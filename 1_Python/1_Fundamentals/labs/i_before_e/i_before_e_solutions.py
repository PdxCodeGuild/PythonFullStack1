'''
Example solution of i before e check()

Check that a word follows "I before E except after C".

>>> check("recieve")
recieve doesn't follow the rule

>>> check("receive")
receive does follow the rule

>>> check("believe")
believe does follow the rule

>>> check("ceiling")
ceiling does follow the rule

>>> check("wierd")
wierd does follow the rule

>>> check("science")
science does not follow the rule

'''

#Very Simple Solution:
def check_yoself(word):
    exceptions = ['science', 'weird',]
    if 'cei' in word:
        result = True
    elif 'cie' in word:
        result = False
    elif 'ei' in word:
        result = False
    elif 'ie' in word:
        result = True

    return result

#Gabby's Solution
def check(word):
    for i, char in enumerate(word):
        if i == len(word)-1:
            break
        next_char = word[i+1]
        print(next_char)
        prev = word[i-1]
        next_two = word[i+1:i+2]

        if char == 'c':
            if next_two == 'ie':
                message = '{} doesn\'t follow the rule'.format(word)
                break
            elif next_two == 'ei':
                message = '{} does follow the rule.'.format(word)
                break
        elif char == 'i' and next_char == 'e' and prev != 'c':
            message = '{} does follow the rule.'.format(word)
            break
        elif char == 'e' and next_char == 'i' and prev != 'c':
            message = '{} doesn\'t follow the rule, e is before i'.format(word)
            break
        else:
            message = '{} does not apply to this test.'.format(word)

    print(message)


# Kieran's Solution
def check(word):
    ie_in_word = 'ie' in word
    ei_in_word = 'ei' in word

    if ie_in_word:
        location = word.index('ie')

        if c_before_ie:
            print('Does not follow ,use ei')

        else:
            print('Follows the rule.')

        c_before_ie =  'c' in word[:location]
        return

    elif ei_in_word:
        location = word.index('ei')

    else:
        raise ValueError('Word {} not applicable.'.format(word))
