OK_FORMAT = True

test = {   'name': 'q5',
    'points': 10,
    'suites': [   {   'cases': [   {'code': ">>> assert if_palindrome('racecar') == True\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> assert if_palindrome('hello') == False\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> assert if_palindrome('12321') == True\n", 'hidden': True, 'locked': False},
                                   {'code': ">>> assert if_palindrome('') == True, 'Empty strings are considred as palindrome too!'\n", 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
