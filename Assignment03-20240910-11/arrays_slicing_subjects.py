# -*- coding: utf-8 -*-
"""Assignment 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1090Ar05uQ9mYNGgt-vx18C-avuY_TSh_
"""

# Write a program to enter the list of 5 subjects and their respective numbers.
# Extract list of marks.

subject_list = [None]*5
marks = [None]*5
i = 0
while(i<=4):
  subject_list[i] = input(f"Enter the name of subject {i} : \n ")
  marks[i] = int(input(f"Enter the marks in subject {i} : \n "))
  i = i+1

print ("List of subjects and marks: ", subject_list, marks)

#extract list of marks
print("Marks : ", marks)