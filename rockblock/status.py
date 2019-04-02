from codes import MO_STATUS_CODES, MT_STATUS_CODES


class SBDStatus:
    def __init__(self, mo_status_code, mo_message_number, mt_status_code, mt_message_number, mt_length, mt_queued):
        self.mo_status_code = mo_status_code
        self.mo_message_number = mo_message_number
        self.mt_status_code = mt_status_code
        self.mt_message_number = mt_message_number
        self.mt_length = mt_length
        self.mt_queued = mt_queued

        self.mo_status_message = self.mo_success = None

        for definition in MO_STATUS_CODES:
            if self.mo_status_code in definition['codes']:
                self.mo_status_message = definition['message']
                self.mo_success = definition['success']
                break

        if not self.mo_status_message:
            raise Exception('Unknown MO status code: {}'.format(self.mo_status_code))

        self.mt_status_message = self.mt_success = None

        for definition in MT_STATUS_CODES:
            if self.mt_status_code in definition['codes']:
                self.mt_status_message = definition['message']
                self.mt_success = definition['success']
                break

        if not self.mt_status_message:
            raise Exception('Unknown MT status code: {}'.format(self.mt_status_code))
