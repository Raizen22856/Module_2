numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
def is_prime(i):
    if i <= 1:
        return
    for k in range(2, int(i ** 0.5) + 1):
        if i % k == 0:
            return False
    return True
for j in range(2, len(numbers) + 1):
    if is_prime(j):
        primes.append(j)
    else:
        not_primes.append(j)
print(primes)
print(not_primes)
