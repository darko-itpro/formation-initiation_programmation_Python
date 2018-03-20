#!/usr/bin/env python


def is_palindrome(sentence):
    """
    Évalue la séquence pour déterminer si c'est un palindrome ou non.

    :param sentence: une chaine de caractères à évaluer
    :type sentence: str
    :return: `True` si c'est un palindrome, `False` sinon
    :type return: bool
    """
    sentence = sentence.lower().replace(' ', '')
    for index, word in enumerate(sentence):
        if word != sentence[-(index + 1)]:
            return False

    return True


if __name__ == '__main__':
    is_palindrome("radar")
