# Problem2 Next Greater Element II (https://leetcode.com/problems/next-greater-element-ii/)
# Time Complexity: O(n),even though we loop through the array two times (2n), each index only gets pushed into the stack once and popped out once. So the total work stays close to n, not n squared.
# Space Complexity: O(n),the stack can hold up to n indices in the worst case and the result list also holds n values.
# Approach:
# We go through the array two times to act like it is circular, without actually copying it.
# We keep a stack of indices that are still waiting to find their next greater number.
# Whenever the current number is bigger than the number at the top of the stack, we know we found the answer for that waiting index, so we pop it and save the answer.

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)  # total number of elements in nums, we will need this to wrap around using modulo

        stack = []  # this will store indices, not values, these are the positions still waiting for their answer

        result = [-1] * n  # start every answer as -1, because if we never find a bigger number, -1 is the correct final answer

        for i in range(2 * n):  # loop two times through the array length to simulate going around the circle once more
            
            while stack and nums[i % n] > nums[stack[-1]]:  
                # keep checking as long as the stack is not empty and the current number is bigger than the number at the top of the stack
                # i % n brings i back into the real index range even after we pass n, this is what makes it circular

                popped_ele = stack.pop()  
                # this index just found its next greater number, so remove it from the stack and hold onto it

                result[popped_ele] = nums[i % n]  
                # save the current number as the answer for the index we just popped

            if i < n:  
                # this only happens during the first pass through the array, using real indices
                stack.append(i)  
                # this number has not found its next greater number yet, so add its index to the stack to wait

            elif stack and stack[-1] == i % n:  
                # this only happens during the second pass
                # if the index on top of the stack is the same as our current wrapped around index, it means we have gone all the way around back to itself
                break  
                # nothing more to check after this, so stop early to save time

        return result  
        # whatever indices are still stuck in the stack never found a bigger number, so they correctly stay -1