def is_palindrome(text: str) -> bool:
    for i in range(len(text) // 2):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True

largest = 0
for i in range(999, 99, -1):
    if i*i < largest:
        break
    for j in range(i, 99, -1):
        num = i*j
        if num < largest:
            break
        if is_palindrome(str(num)):
            largest = num

print(f"The largest palindromic number from the multiplication of two 3-digit numbers is:\n{largest}")
