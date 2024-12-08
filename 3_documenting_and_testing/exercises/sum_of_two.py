#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reviewed and edited on: 08 12 2024

Original Author: Evan Cole
Edited by: Muhammet Isik
No functional changes were made; the code was reviewed and reformatted.
"""
# --- before documenting and testing ---


# def mystery_0(a,b):
#     if a == 0, b==0:
#         return (0)
#     if a == 1,b==1:
#         return (2)
#     if a == 2,b==2:
#         return (4)

#    


# --- after documenting and testing ---


def sum_of_two(a,b):
    """Returns the sum of two integers.

    Parameters:
        a: First integer
        b: Second integer

    Returns:
        int: The sum of the two integers

    >>> sum_of_two(1, 2)
    3

    >>> sum_of_two(-1, 2)
    1

    >>> sum_of_two(0, 0)
    0
    """
# Assert that both inputs are integers
    assert isinstance(a, int), f"Input 'a' should be an integer, got {type(a)}"
    assert isinstance(b, int), f"Input 'b' should be an integer, got {type(b)}"
# 2 Base case: Check if the inputs are integers
    if not isinstance(a, int):
        raise TypeError(f"Input 'a' should be an integer, got {type(a)}")
    if not isinstance(b, int):
        raise TypeError(f"Input 'b' should be an integer, got {type(b)}")
    return a + b
