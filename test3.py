# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rP-zSMZYMJ2dNoxioVZgP_Z-g8PUUSmE
"""

n = int(input())
s = str(n)
rev = s[::-1]
if s == rev:
  print("Это палиндром!")
else:
  print("Это не палиндром!")