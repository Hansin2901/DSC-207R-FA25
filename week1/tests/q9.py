OK_FORMAT = True

test = {   'name': 'q9',
    'points': 10,
    'suites': [   {   'cases': [   {'code': '>>> assert sum(1, 5) == 9\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert sum(-3, 3) == 0\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert sum(5, 5) == 0\n', 'hidden': True, 'locked': False},
                                   {'code': '>>> assert sum(10, 20) == 135\n', 'hidden': True, 'locked': False},
                                   {'code': '>>> assert sum(-5, 0) == -10\n', 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
