def find_first_n_prime_numbers(n: int) -> list[int]:
    assert n >= 1
    found = [2]
    testing = 3
    while len(found) < n:
        is_prime = True 
        for prime in found:
            if testing % prime == 0:
                is_prime = False 
                break
        if is_prime:
            found.append(testing)
        testing += 1
    return found

print(f"The 10001st prime number is:\n{find_first_n_prime_numbers(10001)[-1]}")