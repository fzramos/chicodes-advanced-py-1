import re

def noVowels(word):
    """
    This function will take a string and output only the consanants of the string
    Example:
        Input: 'Joel'
        Output: 'Jl'
    """
    # works but is inefficient/overly long
    # new_word = ''
    # for letter in word:
    #     if letter not in 'aeiou':
    #         new_word += letter
    # return new_word

    # Failed attempt to make it work faster
    # return string([letter for letter in word if letter in 'aeiou'])
    # Efficient way to do it
    # return ''.join('up'+c if c.lower() in 'aeiou' else c for c in word)

    # This regular expression
    pattern = r'[aeiou]'
    return re.sub(pattern, '', word)


if __name__ == "__main__":
    user_in = input("Type a word: ")
    print(noVowels(user_in))
    