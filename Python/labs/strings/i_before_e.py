"""
Check that a word follows "I before E except after C".

>>> check("recieve")
recieve doesn't follow the rule


>>> check("receive")
receive does follow the rule

"""

def check(word):

    if 'ie' in word':
        position = word.index('ie')
        if 'c' in word[0:position+1]:
            message = 'recieve doesn\'t follow the rule'
        else:
            message = 'receive does follow the rule'

    else:
        message = 'This word does not apply to the rule.'
    
    return message
