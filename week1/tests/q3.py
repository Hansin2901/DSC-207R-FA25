OK_FORMAT = True

test = {   'name': 'q3',
    'points': 10,
    'suites': [   {   'cases': [   {'code': '>>> assert is_divisible_by_3(9) == True\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert is_divisible_by_3(-12) == True\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert is_divisible_by_3(7) == False\n', 'hidden': True, 'locked': False},
                                   {'code': '>>> assert is_divisible_by_3(7.5) == False\n', 'hidden': True, 'locked': False},
                                   {'code': ">>> assert is_divisible_by_3('string') == False\n", 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
