# Implemented Errors
The following were the intentional errors that were added to `prime.py`, as well as explainations why they weren't immediately obvious. The solutions these errors are found in `solution.py`.

---
```
...
Line 8:     def range_1_n(limit : int):
...
Line 67:    def is_prime(n : int):
...
```
### 1. None of the the functions check `limit` or `n` to validate it that it's a positive integer.
- While not the most creative error, it's important to provide proper feedback and checks for functions that explicitly show how the function should be used, including what type of data can be passed to it.
---

```
...
Line 11:    results = [2, 3, 5]
...
```

### 2. range_n_1 automatically assumes 2, 3, 5 are on the prime numbers list, even if `limit` < 5
- Edge testing would have to be done with a limit less than 5 in order to see the unintended results. While 2, 3, and 5 are prime numbers, they do not reflect what was inputted by the user.
---

```
...
Line 32:    potentials[n][1] = True
...
Line 41:    potentials[n][1] = True
...
Line 50:    potentials[n][1] = True
...
``` 

### 3. In `range_1_n()`, the potentional's key for adding for each solution is off by one (values starts at key 0, with value 1)
- In some way, it sort of is obvious when you generate the primes, as you'll notice each number past 5 seems to be off by +1. However, you need examine the code carefully to see if it's a key error or calculation error.
---

```
...
Line 48:    n = (3 * x * x) + (y * y)
...
```

### 4. For condition 3, `n` should be expression `(3 * x * x) - (y * y)`
- You have to understand how Sieve of Atkin works to find the error in the expression.
---

```
...
Line 103:   number += (str(random.randint(0, 9)))
...
```

### 5. For `digit_size()`, the method for creating random numbers has an edge case where it's possible to create less than n digit numbers. The solution in `solution.py` is more optimal.
- This is an interesting behavior of typecasting from string to integer in python. The assignment of `number = 0123` would result in a syntax error, but `number = int("0123")` would type cast the string `"0123"` to the integer `123`. Since the previous method would randomly select a chracter from 0 to 9 to append to a string, it was possible the first (and consecutive) digit(s) be 0, shrinking the number when performing the final typecasting.
---


# BONUS

```
...
Line 22:    for x in range(1, limit + 1):
Line 23:        for y in range(1, limit + 1):
...
```
While technically not an error, the runtime for `range_1_n()` is mostly wasted by iterating through loops that will fail to find any potential prime numbers, on the basis that the value of x^2 or y^2 will be fair greater than the `limit`. The implementation in `solution.py` breaks from those loops when the squared variable is greater than the `limit`.

There was also a slight improvement with runtime by having the modulo conditional statements modified so that limit checks on `n` and the polarity relationship of `x` and `y` were checked first before checking the remainder of `n`.
