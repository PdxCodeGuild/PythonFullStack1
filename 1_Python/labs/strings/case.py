"""
>>> which_case('this_test_text')
'snake_case.'

>>> which_case('this_is_snake_case')
'snake_case.'

>>> which_case('ThisIsCamelCase')
'CamelCase.'

### Advanced ###

>>>snake_to_camel('this_is_snake_case')
'ThisIsSnakeCase'

>>>camel_to_snake('ThisIsCamelCase')
'this_is_camel_case'


"""
