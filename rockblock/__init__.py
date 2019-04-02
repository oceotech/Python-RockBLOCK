from serial import Serial
from time import time
from re import match
from status import SBDStatus

ROCKBLOCK_BAUD_RATE = 19200
ROCKBLOCK_GENERAL_TIMEOUT = 0.5 # 0.5 seconds
ROCKBLOCK_SEND_TIMEOUT = 30 # 30 seconds


class RockBLOCK:
    def __init__(self, path):
        self.serial = Serial(path, ROCKBLOCK_BAUD_RATE)
        self.status = None

    def init(self):
        # Disable echo
        self.__writeCommand('ATE0')
        self.__matchResponse(r'OK')

        # Disable flow control
        self.__writeCommand('AT&K0')
        self.__matchResponse(r'OK')

    def send(self, message):
        # Load message into M0 buffer
        self.__writeCommand('AT+SBDWT={}'.format(message))
        self.__matchResponse(r'OK')

        return self.__initiateExtendedSBDSession(ROCKBLOCK_SEND_TIMEOUT)

    def checkSignalStrength(self):
        # Request signal quality
        self.__writeCommand('AT+CSQ')

        result = self.__matchResponse(r'\+CSQ:(\d)')

        # Cast to int, 0 is no signal, 5 is full strength
        return int(result.group(1))

    def __initiateExtendedSBDSession(self, timeout=ROCKBLOCK_GENERAL_TIMEOUT):
        # Initiate extended SBD session
        self.__writeCommand('AT+SBDIX')

        result = self.__matchResponse(r'\+SBDIX:\ (\d+),\ (\d+),\ (\d+),\ (\d+),\ (\d+),\ (\d+)', timeout)

        mo_status_code = int(result.group(1))
        mo_message_number = int(result.group(2))
        mt_status_code = int(result.group(3))
        mt_message_number = int(result.group(4))
        mt_length = int(result.group(5))
        mt_queued = int(result.group(6))

        self.status = SBDStatus(mo_status_code, mo_message_number, mt_status_code, mt_message_number, mt_length, mt_queued)

        return self.status

    def __matchResponse(self, pattern, timeout=ROCKBLOCK_GENERAL_TIMEOUT):
        finish_time = time() + timeout

        while True:
            # Calculate the time remaining and modify serial stream timeout
            time_remaining = finish_time - time()
            self.serial.timeout = max(0, time_remaining)

            line = self.serial.read_until('\r').strip()

            # Check to see if line matches pattern
            result = match(pattern, line)

            if result is not None:
                return result

            # Raise exception if time is up
            if time_remaining < 0:
                raise Exception('Timeout waiting for expected response')

    def __writeCommand(self, command):
        self.serial.write('{}\r'.format(command))
