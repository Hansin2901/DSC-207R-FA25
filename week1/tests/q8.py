OK_FORMAT = True

test = {   'name': 'q8',
    'points': 10,
    'suites': [   {   'cases': [   {'code': ">>> assert remove_vowels('Hello, World!') == 'Hll, Wrld!'\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> assert remove_vowels('Python Programming') == 'Pythn Prgrmmng'\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> assert remove_vowels('AEIOUaeiou') == ''\n", 'hidden': True, 'locked': False},
                                   {'code': ">>> assert remove_vowels('') == ''\n", 'hidden': True, 'locked': False},
                                   {'code': ">>> assert remove_vowels('12345') == '12345'\n", 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
