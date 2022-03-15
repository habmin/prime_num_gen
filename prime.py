import random

# --- Prime number generator by range ---
# Finds all the prime numbers from 1 to <limit> (inclusive)
# Generates numbers based off of the Sieve of Atkin
# ref: https://en.wikipedia.org/wiki/Sieve_of_Atkin
# Precondition: limit must be a positive integer
def range_1_n(limit : int):
    # --- Initializers ---
    # Results list contains all prime numbers
    results = [2, 3, 5]
    
    # Potential list will store a the range from 1 to limit,
    # Each cell is the number and if it is marked prime or not
    # Starting off with every number marked not prime
    potentials = []
    for i in range(1, limit + 1):
        potentials.append([i, False])

    # --- Sieve of Atkin Implimentation ---
    # Use all positive integers of x and y for finding possible solutions for n
    for x in range(1, limit + 1):
        for y in range(1, limit + 1):
            
            # Condition 1:
            # for all solutions where the remainder of n = 4x^2 + y^2 modulo 60 is 
            # 1, 13, 17, 29, 37, 41, 49, and 53
            # and where x is all numbers and y is odd
            # label that number as potentionally prime
            n = (4 * x * x) + (y * y)
            if n % 60 in [1, 13, 17, 29, 37, 41, 49, 53] and n <= limit and y % 2 == 1:
                potentials[n][1] = True

            # Condition 2:
            # for all solutions where the remainder of n = 3x^2 + y^2 modulo 60 is 
            # 7, 19, 31, 43
            # and where x is odd and y is even
            # label that number as potentionally prime
            n = (3 * x * x) + (y * y)
            if n % 60 in [7, 19, 31, 43] and n <= limit and x % 2 == 1 and y % 2 == 0:
                potentials[n][1] = True
            
            # Condition 3:
            # for all solutions where the remainder of n = 3x^2 - y^2 modulo 60 is 
            # 11, 23, 47, 59
            # and where x and y is an even/odd or odd/even combo
            # label that number as potentionally prime
            n = (3 * x * x) + (y * y)
            if x > y and n % 60 in [11, 23, 47, 59] and n <= limit and y % 2 == (x - 1) % 2:
                potentials[n][1] = True

    # --- Remove perfect squares from the potentials list
    for i in range(len(potentials)):
        if potentials[i][1]:
            power = potentials[i][0] * potentials[i][0]
            for j in range(power, limit, power):
                potentials[j][1] = False
    
    # --- Extract prime numbers from potentional list and output results
    for n in potentials:
        if n[1]:
            results.append(n[0])
    print(results)

# --- Helper function to determine if n is prime ---
# Precondition: n must be a positive integer
def is_prime(n : int):
    # Manually return 1 as False
    if n == 1:
        return False
    
    # Loop through integer i, starting at 2 and up until the square
    # of i is greater than the value of n
    # If n is divisable by i, that means n is a perfect square
    # and is not a prime number.
    # Otherwise, the number is prime
    # Note: while when n = 2 or n = 3 technically never enter the loop
    # they are prime numbers and will return true
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# --- Generate a set of random prime numbers by a digit size ---
# Will generate a number number that has <digits> amount of digits
# Then check if the number is prime
# This prime number generator will continue finding random prime numbers
# Until a <total> amount is found
# Precondition: <digits> and <total> must be positive integers
def digit_size(digits : int, total : int):
    # --- Initializer ---
    results = []

    # --- Loop ---
    # Continues until the results list has <total> amount of entries
    while len(results) < total:
        number = ""

        # Keep adding a random integer until the <digit> length is reached
        for i in range(digits - 1):
            number += (str(random.randint(0, 9)))
        
        # If the number is prime, add it to results
        if is_prime(int(number)):
            results.append(int(number))

    print(results)
