"""
Write a function that returns true if the input is a palindrome, or false, if it is not.

>>> palindrome('hannah')
True
>>> palindrome('racecar')
True
>>> palindrome('a man, a plan, a canal, Panama')
True
>>> palindrome("1 pound coconut.")
False
>>> palindrome(1234321)
True
"""

def scrub_text(text):

    clean_text = str(text).strip().replace(",", '').replce(" ", '').replace(".", '').lower()

    return clean_text


def palindrome(candidate):
    """
    Returns True or False if the input param is a palindrome.
    """
     text = scrub_text(candidate)


    if text == text[::-1]:
        return True
    else:
        return False

   
