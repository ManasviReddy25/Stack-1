# Problem1 Daily Temperatures (https://leetcode.com/problems/daily-temperatures/)
# Time Complexity: O(n),each index goes into the stack exactly once and comes out of the stack at most once. So across the whole loop, total pushes and pops add up to about 2n, which is still O(n) overall, even though there is a while loop inside a for loop.
# Space Complexity: O(n),the result array always uses n space. The stack can also hold up to n indices in the worst case, like when temperatures keep decreasing and nothing ever gets popped.
# Approach:
# We use a stack to keep track of indices whose warmer day we have not found yet.
# For each new day, we check if it is warmer than the day on top of the stack.
# If yes, we pop that day off and record how many days it waited, and we keep
# doing this until the stack is empty or today is no longer warmer.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)  # total number of days, used to size the result array
        stack = []  # stores indices of days that are still waiting for a warmer day
        result = [0] * n  # start every answer at 0, since some days may never find a warmer day

        for i in range(n):  # go through each day one by one using its index
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # stack[-1] is the index of the most recent waiting day
                # if today is warmer than that waiting day, we just found its answer
                popped_temp = stack.pop()  # remove that waiting day, we are done waiting for it
                result[popped_temp] = i - popped_temp  # wait time is today's index minus that day's index

            stack.append(i)  # today has not found a warmer day yet, so it waits on the stack

        return result  # after processing all days, this holds the final wait counts