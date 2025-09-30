OK_FORMAT = True

test = {   'name': 'q4',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> assert x.shape == (3, 5)\n',
                                       'failure_message': "The broadcast result changed shape. Ensure you're adding a 1D vector so NumPy broadcasts across the columns without altering dimensions. "
                                                          'Check if your 2 initial arrays that you are adding have expected shapes.',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> assert not np.array_equal(x, a)\n',
                                       'failure_message': "x still matches a. Confirm you're adding vector c elementwise so the broadcast sum changes the entries.",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
