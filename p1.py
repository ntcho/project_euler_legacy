# Target number used to limit iteration
# Since it's defined in the problem as 'below 1000', it shouldn't contain 1000.
k = 999

# Initial idea method, O(1)

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

print(f'{sum[0]} + {sum[1]} - {sum[2]} = {sum[0] + sum[1] - sum[2]}')

# Bruteforce method, O(n)

s = 0
for i in range(1000):
    if i % 3 is 0 or i % 5 is 0:
        s += i

print(s)

# Function method (from overview), O(1)