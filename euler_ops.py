import math

#Prints the answer to the Project Euler problem
def print_answer(answer, argList):
    problem_number = argList[0].replace("euler_", "")
    problem_number = problem_number.replace(".py", "")
    print ("The answer to Project Euler problem", problem_number, "is:", answer)

#Sums all the multiples of a number
def sum_multiples(min, max, multiple):
    sum = 0
    start = min + multiple - (min % multiple)
    for i in range(start, max, multiple):
        sum += i
    return sum

#Finds the largest prime factor of a number
def largest_prime_factor(number):
    prime_found = False
    count = number - 1
    is_prime = True
    #ensure number is odd so -2 increment can be used
    if(count % 2) is 0:
        count -= 1
    while not prime_found:
        print (count, "\n")
        if (number % count) is 0:
            is_prime = is_prime(count)
            if is_prime is True:
                prime_found = True
        count -= 2
        is_prime = True
    return count + 1

#Evaluates whether a number is even or not
def is_even(number):
    if number % 2 is 0:
        return True
    elif number % 2 is 1:
        return False

#Evaluates whether a number is prime or not
def is_prime(number):
    is_prime = True
    count = 3
    max = math.sqrt(number)
    while (is_prime and count <= max) is True:
        if (number % count) is 0:
            is_prime = False
        count += 2
    return is_prime

#Multiplies all the primes from 2 to number inclusive
def mult_primes(number):
    product = 2
    for i in range(3, number + 1, 2):
        if is_prime(i) is True:
            product *= i
    return product

#Adds all the primes from 2 to number inclusive
def sum_primes(number):
    sum = 2
    for i in range(3, number + 1, 2):
        if is_prime(i) is True:
            sum += i
    return sum

#Sums all the numbers up to a number inclusive
def sum_numbers(number):
    sum_numbers = 0
    for i in range(1, number + 1):
        sum_numbers += i
    return sum_numbers

#Sums all the squares of numbers up to a number inclusive
def sum_squares(number):
    sum_squares = 0
    for i in range(1, number + 1):
        sum_squares += i * i
    return sum_squares

#Finds the ith prime(number)
def find_ith_prime(number):
    if number is 1:
        return 2
    count = 3
    count_primes = 2
    while count_primes <= number:
        if is_prime(count) is True:
            count_primes += 1
        count += 2
    return count - 2
