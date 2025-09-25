OK_FORMAT = True

test = {   'name': 'q1',
    'points': 5,
    'suites': [   {   'cases': [   {'code': '>>> assert type(my_int) == str\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert type(my_str) == int\n', 'hidden': False, 'locked': False},
                                   {'code': ">>> assert my_int == 'Hi'\n", 'hidden': True, 'locked': False},
                                   {'code': '>>> assert my_str == 5\n', 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
