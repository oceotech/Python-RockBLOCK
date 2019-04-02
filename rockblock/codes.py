MO_STATUS_CODES = [
    {
        'codes': [0],
        'message': 'M0 message, if any, transferred successfully',
        'success': True,
    },
    {
        'codes': [1],
        'message': 'MO message, if any, transferred successfully, but the MT message in the queue was too big to be transferred',
        'success': True,
    },
    {
        'codes': [2],
        'message': 'MO message, if any, transferred successfully, but the requested Location Update was not accepted',
        'success': True,
    },
    {
        'codes': [3, 4],
        'message': 'Reserved, but indicate MO session success if used',
        'success': True,
    },
    {
        'codes': [5, 6, 7, 8, 9],
        'message': 'Reserved, but indicate MO session failure if used',
        'success': False,
    },
    {
        'codes': [10],
        'message': 'GSS reported that the call did not complete in the allowed time',
        'success': False,
    },
    {
        'codes': [11],
        'message': 'MO message queue at the GSS is full',
        'success': False,
    },
    {
        'codes': [12],
        'message': 'MO message has too many segments',
        'success': False,
    },
    {
        'codes': [13],
        'message': 'GSS reported that the session did not complete',
        'success': False,
    },
    {
        'codes': [14],
        'message': 'Invalid segment size',
        'success': False,
    },
    {
        'codes': [15],
        'message': 'Access is denied',
        'success': False,
    },
    {
        'codes': [16],
        'message': 'ISU has been locked and may not make SBD calls (see +CULK command)',
        'success': False,
    },
    {
        'codes': [17],
        'message': 'Gateway not responding (local session timeout)',
        'success': False,
    },
    {
        'codes': [18],
        'message': 'Connection lost (RF drop)',
        'success': False,
    },
    {
        'codes': [19],
        'message': 'Link failure (A protocol error caused termination of the call)',
        'success': False,
    },
    {
        'codes': range(20, 31 + 1),
        'message': 'Reserved, but indicate failure if used',
        'success': False,
    },
    {
        'codes': [32],
        'message': 'No network service, unable to initiate call',
        'success': False,
    },
    {
        'codes': [33],
        'message': 'Antenna fault, unable to initiate call',
        'success': False,
    },
    {
        'codes': [34],
        'message': 'Radio is disabled, unable to initiate call (see *Rn command) ',
        'success': False,
    },
    {
        'codes': [35],
        'message': 'ISU is busy, unable to initiate call',
        'success': False,
    },
    {
        'codes': [36],
        'message': 'Try later, must wait 3 minutes since last registration',
        'success': False,
    },
    {
        'codes': [37],
        'message': 'SBD service is temporarily disabled',
        'success': False,
    },
    {
        'codes': [38],
        'message': 'Try later, traffic management period (see +SBDLOE command)',
        'success': False,
    },
    {
        'codes': range(39, 63 + 1),
        'message': 'Reserved, but indicate failure if used',
        'success': False,
    },
    {
        'codes': [64],
        'message': 'Band violation (attempt to transmit outside permitted frequency band)',
        'success': False,
    },
    {
        'codes': [65],
        'message': 'PLL lock failure; hardware error during attempted transmit',
        'success': False,
    },
]

MT_STATUS_CODES = [
    {
        'codes': [0],
        'message': 'No SBD message to receive from the GSS',
        'success': True,
    },
    {
        'codes': [1],
        'message': 'SBD message successfully received from the GSS',
        'success': True,
    },
    {
        'codes': [2],
        'message': 'An error occurred while attempting to perform a mailbox check or receive a message from the GSS',
        'success': False,
    },
]
