# -*- coding: utf-8 -*-
"""assignment6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ndlduJVs11rKCCL8yacYv8nKVFlGFir_
"""

# Print fibonacci series
def fibo(n):
    a = 0
    b = 1
    count = 0
    while(count < n):
        print(a)
        sum = a + b
        a = b
        b = sum
        count = count+1

n = int(input("Enter the number until which you want to print your fibonacci series : "))
if(n <= 0):
    print("Invalid input!!! Please re-run with a positive numbergreater than 0")
else:
    fibo(n)