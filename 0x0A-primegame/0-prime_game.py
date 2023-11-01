#!/usr/bin/python3

"""
   Module for Prime Game question
"""


def prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
    if flag:
        return flag
    else:
        return False


def isWinner(x, nums):
    """
    A function that solves a short prime number question
    params:
    x - X is the time a round lasts
    nums - An array to pick numbers from
    """
    if not nums or x < 1:
        return None
    max_num = max(nums)

    my_filter = [True for _ in range(max(max_num + 1, 2))]
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not my_filter[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            my_filter[j] = False
    my_filter[0] = my_filter[1] = False
    y = 0
    for i in range(len(my_filter)):
        if my_filter[i]:
            y += 1
        my_filter[i] = y
    player1 = 0
    for x in nums:
        player1 += my_filter[x] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
