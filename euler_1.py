import euler_ops
import sys

sum_mult_5_3 = (euler_ops.sum_multiples(0, 1000, 3)
               + euler_ops.sum_multiples(0, 1000, 5)
               - euler_ops.sum_multiples(0, 1000, 15))
euler_ops.print_answer(sum_mult_5_3, sys.argv)
