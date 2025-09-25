OK_FORMAT = True

test = {   'name': 'q4',
    'points': 10,
    'suites': [   {   'cases': [   {   'code': '>>> assert has_three_digits(\'123\') is True, "\'123\' should be valid: exactly three digits"\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 1.5,
                                       'success_message': 'Passed basic case 1/5'},
                                   {   'code': '>>> assert has_three_digits(\'234\') is True, "\'234\' should be valid: exactly three digits"\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 1.5,
                                       'success_message': 'Passed basic case 2/5'},
                                   {   'code': '>>> assert has_three_digits(\'456\') is True, "\'456\' should be valid: exactly three digits"\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 1.5,
                                       'success_message': 'Passed basic case 3/5'},
                                   {   'code': '>>> assert has_three_digits(\'789\') is True, "\'789\' should be valid: exactly three digits"\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 1.5,
                                       'success_message': 'Passed basic case 4/5'},
                                   {   'code': '>>> assert has_three_digits(\'999\') is True, "\'999\' should be valid: exactly three digits"\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 1.5,
                                       'success_message': 'Passed basic case 5/5'},
                                   {   'code': '>>> assert has_three_digits(\'012\') is False, "\'012\' -> \'12\' so it\'s not three digits after ignoring leading zeros"\n'
                                               '>>> assert has_three_digits(\'0123\') is True, "\'0123\' -> \'123\' so it should be valid (three digits after ignoring leading zeros)"\n'
                                               '>>> assert has_three_digits(\'99\') is False, "Too few digits: \'99\' should be invalid (need exactly three after ignoring leading zeros)"\n'
                                               '>>> assert has_three_digits(\'1000\') is False, "Too many digits: \'1000\' should be invalid (need exactly three)"\n'
                                               '>>> assert has_three_digits(\' 123 \') is True, "Whitespace should be ignored: \' 123 \' should be valid"\n'
                                               '>>> assert has_three_digits(\'-123\') is False, "Negative sign not allowed: \'-123\' should be invalid per prompt"\n'
                                               '>>> assert has_three_digits(\'12.3\') is False, "Decimal point not allowed: \'12.3\' should be invalid"\n'
                                               '>>> assert has_three_digits(123) is True, "Non-string inputs are cast to string; 123 should be valid as \'123\'"\n'
                                               ">>> assert has_three_digits(None) is False, 'None should be invalid (cannot represent a three-digit positive integer)'\n",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 2.5,
                                       'success_message': 'Passed all edge cases'}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
