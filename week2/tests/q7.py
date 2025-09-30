OK_FORMAT = True

test = {   'name': 'q7',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> assert X.shape == (3, 5)\n',
                                       'failure_message': "X should stay 3 by 5. Swap the first two rows without changing the array's shape.",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> assert Y.shape == (3, 5)\n',
                                       'failure_message': "Y should remain 3 by 5 after the column swap. Check that you're exchanging the correct columns.",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
