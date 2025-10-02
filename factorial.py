def factorial(n: int) -> int:
    """
    Compute the factorial of a number n.
    Example:
        factorial(5) -> 120
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# Demo usage
if __name__ == "__main__":
    print(factorial(5))   # 120
    print(factorial(0))   # 1
    print(factorial(7))   # 5040
