import euler_ops
import sys
import math

number_max = 20
increment = euler_ops.mult_primes(number_max)
count = increment
min_divisor = math.floor(number_max / 2)
divisor = 0
is_evenly_divisible = False
current_divisible = True
while is_evenly_divisible is False:
    current_divisible = True
    divisor = min_divisor
    while current_divisible is True and divisor <= number_max:
        if count % divisor is not 0:
            current_divisible = False
        divisor += 1
    if current_divisible is True:
        is_evenly_divisible = True
    else:
        count += increment

euler_ops.print_answer(count, sys.argv)
