#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Dec 7, 2024

@author: Muhammet Isik
"""
import unittest

# --- imports & test class before documenting and testing ---

# from ..sum_of_two import sum_of_two

# class TestSumOfTwo(unittest.TestCase):

# --- imports & test class after documenting and testing ---
from ..sum_of_two import sum_of_two

class TestSumOfTwo(unittest.TestCase):
    """Test the sum_of_two function"""
    
    def test_positives(self):
        """It should correctly add two positive integers"""
        actual = sum_of_two(1, 2)# call function with test arguments
        expected = 3 # hand-write the expected return value
        self.assertEqual(actual, expected)
    def test_negatives_and_positives(self):
        """It should correctly add one negative and one positive integers"""
        actual = sum_of_two(-1,2)
        expected = 1 
        self.assertEqual(actual, expected)  
    def test_zeros(self):
        """It should give 0 to sum of two zeros."""
        actual = sum_of_two(0,0)
        expected = 0
        self.assertEqual(actual, expected)
    def test_negative_numbers(self):
        """It should correctly add two negative integers"""
        actual = sum_of_two(-5, -3)
        expected = -8
        self.assertEqual(actual, expected)

    def test_large_numbers(self):
        """It should handle large numbers correctly"""
        self.assertEqual(sum_of_two(999999999, 1000000000), 1999999999)

    def test_not_an_integer(self):
        """It should raise an AssertionError if the argument is not an integer"""
        with self.assertRaises(AssertionError):
            sum_of_two("a", 2)
