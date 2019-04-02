# RockBLOCK - Python Library

RockBLOCK modem driver for use of the Iridium SBD service.

## Install

```sh
pip install rockblock
```

## Usage

```py
from rockblock import RockBLOCK

r = RockBLOCK('/dev/ttyUSB0')

# This will throw an exception if there is an error
r.init()

# Returns an int from 0-5 (no signal - full strength)
signal_strength = r.checkSignalStrength()

# Returns an SBDStatus object
status = r.send('Hello!')

# Check for MO error
if not status.mo_success:
    print('MO Error: {}'.format(status.mo_status_message))

# Check for MT error
if not status.mt_success:
    print('MT Error: {}'.format(status.mt_status_message))
```
