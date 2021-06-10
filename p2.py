'''Problem 2: Even Fibonacci numbers
https://projecteuler.net/problem=2

Key idea
- testing first few iterations for patterns (especially when thousands of 
  iterations are estimated)
'''


'''Initial idea, O(n)'''

k = 4000000
sum = 0

def fibo(a, b):
    if a % 2 is 0:
        global sum  # NOTE: Keyword `global` is required to change the global 
                    #       variable in a function in Python.
        sum += a

    if b < k:
        fibo(b, a + b)  # NOTE: Use loops over recursions for performance.

fibo(1, 2)

print(str(sum))


'''Loop method (from overview), O(n)'''

a = 1
b = 2
sum = 0

while b < k:
    if b % 2 is 0:
        sum += b
    c = a + b
    a = b
    b = c

print(str(sum))


'''Every third number method (from overview), O(n/3)'''
# Key idea: testing first few iterations
# fibonacci = 1 1 2 3 5 8 13 21 34 55 89 144 ...
# even numbers =  ^     ^       ^^       ^^^

sum = 0

a = 1
b = 1
c = a + b

while c < k:
    sum += c  # Third iteration is always even number
    a = b + c
    b = c + a
    c = a + b

print(str(sum))
