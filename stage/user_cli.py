#!/usr/bin/env python 
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from stage import palindrom

    mot = input('Proposez un mot')

    print("C'est un palindrome"
          if palindrom.is_palindrome(mot)
          else "Ce n'est pas un palindrome")
