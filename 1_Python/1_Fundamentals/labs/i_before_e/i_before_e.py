"""
Check that a word follows "I before E except after C".

>>> check("recieve")
recieve doesn't follow the rule

>>> check("receive")
receive does follow the rule

>>> check("believe")
believe does follow the rule

>>> check("ceiling")
ceiling does follow the rule

>>> check("weird")
weird does not follow the rule

>>> check("science")
science does not follow the rule

"""
