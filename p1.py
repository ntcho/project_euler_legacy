'''Problem 1: Multiples of 3 and 5
https://projecteuler.net/problem=1

Key idea
- using mathematical concepts to reduce the iteration number
'''

# Target number used to limit iteration
# Since it's defined in the problem as 'below 1000', it shouldn't contain 1000.
# NOTE: Clarify the range of the problem before diving into it.
k = 999


'''Initial idea, O(1)'''

f = [3, 5, 15]  # factors
n = [k//3, k//5, k//15]  # number of multiples
max = [k - k%3, k - k%5, k - k%15]  # biggest multiples for each factor 
sum = []  # sum of each factors

for i in range(3):
    minmax = f[i] + max[i]
    s = (n[i] // 2) * minmax

    if n[i] % 2 is 1:
        s += minmax // 2

    sum.append(s)

# print(f'{sum[0]} + {sum[1]} - {sum[2]} = {sum[0] + sum[1] - sum[2]}')
print(str(sum[0] + sum[1] - sum[2]))


'''Bruteforce method, O(n)'''

s = 0
for i in range(1000):
    if i % 3 is 0 or i % 5 is 0:
        s += i

print(s)


'''Function method (from overview), O(1)'''
# NOTE: Use functons or external blocks for complicated for loops or loops with
#       small iteration count.

def get_multiple_sum(f):
    n = k // f
    max = k - k % f
    sum = (f + max) * (n // 2)

    if n % 2 is 1:
        sum += (f + max) // 2

    return sum

print(str(get_multiple_sum(3) + get_multiple_sum(5) - get_multiple_sum(15)))