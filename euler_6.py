import euler_ops
import sys

number = 100
sum_num = euler_ops.sum_numbers(number)
sum_squ = euler_ops.sum_squares(number)
answer = (sum_num * sum_num) - sum_squ
euler_ops.print_answer(answer, sys.argv)
