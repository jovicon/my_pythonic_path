'''
number: 7
name: Reverse Integer
dificulty: Easy 
url: https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

'''

class Solution:
    def reverse(self, x: int) -> int:
        

        if self.check_enviroment_32_bit(x):

            string_integer = str(x)
            if string_integer[0] == '-' and self.check_enviroment_32_bit(int("-"+ string_integer[:0:-1])):
                return int("-"+ string_integer[:0:-1])
            elif string_integer[0] != '-' and self.check_enviroment_32_bit(int(string_integer[::-1])):
                return int(string_integer[::-1])
            else:
                return 0
        
        return 0
    
    
    def check_enviroment_32_bit (self, number:int) -> bool:
        absolute_max_pos = (2 ** 31) - 1
        absolute_max_neg = -(2 ** 31)
        
        return number <= absolute_max_pos and number >= absolute_max_neg