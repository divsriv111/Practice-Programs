def mySqrt(x) -> int:
    if x == 0:
        return 0
    last_guess = x / 2.0
    while True:
        guess = (last_guess + x / last_guess) / 2
        if abs(guess - last_guess) < 0.000001:  # example threshold
            return int(guess)
        last_guess = guess


n = int(input())
print(mySqrt(n))
