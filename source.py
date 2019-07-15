def factorial(n):
  
        if n==1:
            return 1
        else:
            return n*factorial(n-1)
n=int(input())
if (n>=2 and n<=12):
    print(factorial(n))
