"""
Comparing Algorithms to find the smallest number in list
"""


import datetime
import random


def sol1(input_list):
    start_time = datetime.datetime.now()
    # create a list
    # find min value using loop
    min_val = input_list[0]
    min_val_idx = 0

    for val in input_list:
        if val < min_val:
            min_val = val
            min_val_idx = input_list.index(val)
    # display the min value
    return datetime.datetime.now() - start_time, min_val, min_val_idx


def sol2(input_list):
    start_time = datetime.datetime.now()
    # find min value using loop
    min_val = input_list[0]
    min_val_idx = 0
    for i in range(len(input_list)):
        if input_list[i] < min_val:
            min_val = input_list[i]
            min_val_idx = i
    return datetime.datetime.now() - start_time, min_val, min_val_idx


def sol3(input_list):
    start_time = datetime.datetime.now()
    # create a list
    # find min value
    min_val = min(input_list)
    # find all indices corresponding to min val
    min_val_idx = [i for i in range(len(input_list)) if input_list[i] == min_val]
    return datetime.datetime.now() - start_time, min_val, min_val_idx


def print_results(sol_result, sol_x):
    print(f'the number {sol_result[1]} index: {sol_result[2]} \nand the runtime is {sol_result[0]} for {sol_x} ')


if __name__ == '__main__':
    ls = [random.randint(44, 99999999999999999999999999) for x in range(0, 1000000)]
    print_results(sol3(ls), 'sol3')
    print_results(sol2(ls), 'sol2')
    print_results(sol2(ls), 'sol1')
