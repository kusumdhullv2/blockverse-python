# -*- coding: utf-8 -*-
"""
Assignment1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DTcoAPkjETQB1GXfWYqVVWEqhWyFNPm0
"""

# program to check if entered year is leap or not
def is_leap_year(year):
  # 
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
   return True
  else:
   return False

year = int(input("Enter the year..."))

if is_leap_year(year):
     print(f"Yes, {year} is a leap year.")
else:
     print(f"No, {year} is not leap year.")
