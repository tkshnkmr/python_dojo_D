import os, sys

x_val=1
my_name='name'

def my_method(x_val: int, y_val: str) -> int:
   # No doc string + No typing
   return x_val + y_val


# Long comment, Long comment, Long comment, Long comment, Long comment, Long comment, Long comment, Long comment, 
y_val=2

z_val = my_method(x_val=x_val, y_val=y_val)

z_ls = [1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 100, 200, 1000, 5000, 6000, 10, 100, 200, 300]
