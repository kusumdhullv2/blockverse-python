# -*- coding: utf-8 -*-
"""Assignment3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nAc28ONMZ26WyEJ5LHP1wHwy-FPyLvTR
"""

# Print given name diagonally
name = input("Enter the name you want to print : ")
rows = len(name)
#print(rows)

for i in range(0, rows):
  for j in range(0, rows):
    if i == j:
      print( name[j] , end = "")
    else:
      print( "*" , end = "")
  print()