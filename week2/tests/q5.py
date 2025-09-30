OK_FORMAT = True

test = {   'name': 'q5',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> assert z.shape == (3, 5)\n',
                                       'failure_message': "z should remain 3 by 5. Check how you're reshaping B before broadcasting so the dimensions stay intact.",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> assert not np.array_equal(z, a)\n',
                                       'failure_message': "z still matches a. Ensure you're adding the reshaped column vector rather than the original list.",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
