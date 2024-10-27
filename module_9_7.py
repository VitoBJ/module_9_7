def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if result <= 1:
            print("Составное")
            return result

        for i in range(2, int(result**0.5) + 1):
            if result % i == 0:
                print("Составное")
                return result
        print("Простое")
        return result

    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c


print(sum_three(1, 2, 3))
print(sum_three(2, 3, 5))
print(sum_three(1, 1, 1))
print(sum_three(0, 1, 0))
print(sum_three(3, 5, 7))