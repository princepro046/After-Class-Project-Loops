def power(base, exponent):
    result = 1
    # Loop to multiply base 'exponent' times
    for _ in range(abs(exponent)):
        result *= base
    
    # If exponent is negative, return the reciprocal
    if exponent < 0:
        result = 1 / result
    
    return result

# Taking input from the user
base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent (n): "))

# Calculating power
result = power(base, exponent)

# Printing the result
print(f"{base} raised to the power {exponent} is: {result}")
