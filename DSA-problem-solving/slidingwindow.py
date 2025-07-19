


# Find the maximum sum of any contiguous subarray of size K
""" 
nums = [2, 1, 5, 1, 3, 2]
k = 3
res = 9
"""
"""
nums = [2, 1, 5, 1, 3, 2]
k = 3

max_sum = current_sum = sum(nums[:3])
# 2, 1, 5 => 8 

for i in range(k,len(nums)):
    current_sum += nums[i] - nums[i-k]
    print(current_sum)
    if current_sum > max_sum:
        max_sum = current_sum

# print(max_sum)

# Find the minimum sum of any contiguous subarray of size K

min_sum = current_sum = sum(nums[:k])

for i in range(k, len(nums)):
    current_sum += nums[i] - nums[i-k]
    # print(current_sum)
    
    if current_sum < min_sum:
        min_sum = current_sum
        
print(min_sum)

"""
# ============================================================ 
""" 
Given an array of integers nums and an integer k, return an array containing the average of every contiguous subarray of size k.
nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
[2.2, 2.8, 2.4, 3.6, 2.8]
"""
"""
nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5

current_sum = sum(nums[:k])

average_list = []
average_list.append(current_sum/k)

for i in range(k, len(nums)):
    
    current_sum += nums[i] - nums[i-k]
    
    average_list.append(current_sum/k)
    
print(average_list)

"""

#########################################################################
# from collections import defaultdict
"""
s = "cbaebabacd"
p = "abc"

p_len = len(p)
s_len = len(s)


p_count = defaultdict(int)
window_count = defaultdict(int)

# Initialize frequency maps for p and the first window in s
for i in range(p_len):
    p_count[p[i]] += 1
    window_count[s[i]] += 1
    
result = 0
if window_count == p_count:
    result += 1

# Slide the window
for i in range(p_len, s_len):
    # Remove the outgoing character (leftmost)
    outgoing_char = s[i - p_len]
    if window_count[outgoing_char] == 1:
        del window_count[outgoing_char]
    else:
        window_count[outgoing_char] -= 1
    
    # Add the incoming character (rightmost)
    incoming_char = s[i]
    window_count[incoming_char] += 1
    
    # Check if current window is an anagram
    if window_count == p_count:
        result += 1

"""
############################################################
"""
def generate_permutations(s):
    def backtrack(path, counter):
        if len(path) == len(s):
            result.append("".join(path))
            return
        for char in counter:
            if counter[char] > 0:
                path.append(char)
                counter[char] -= 1
                backtrack(path, counter)
                path.pop()
                counter[char] += 1

    from collections import Counter
    result = []
    backtrack([], Counter(s))
    return result

# Example
print(generate_permutations("aab")) 
"""  

##############################################################
"""
Given a string s and an integer k, find the length of the longest substring that contains at most k distinct characters.

Examples
Input: s = "eceba", k = 2
Output: 3
Explanation: The longest substrings with at most 2 distinct characters are "ece" (with 'e' and 'c') and "ceb" (with 'c' and 'e').

"""
