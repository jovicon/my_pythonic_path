'''
number: 1122 
name: Relative Sort Array
dificulty: Easy 
url: https://leetcode.com/problems/relative-sort-array/

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
 

Constraints:

arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
Each arr2[i] is distinct.
Each arr2[i] is in arr1.

'''

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        pivot_front = 0
        
        # hash arr2
        hash_arr2 = {}
        for i,num_2 in enumerate(arr2):
            hash_arr2[num_2] = i
            
        # in
        index_in = []
        not_in = []
        for j,num_1 in enumerate(arr1):
            
            if num_1 in arr2:
                index_in.append(hash_arr2[num_1]) 
            else:
                not_in.append(num_1)   
        
        index_in.sort()

        
        arr_in = []
        for index in index_in:
            arr_in.append(arr2[index])
        
        
        not_in.sort()
        arr_in.extend(not_in)
        
        return arr_in