
Length of Longest Increasing Subsequence (LIS):
https://leetcode.com/problems/longest-increasing-subsequence/description/

Problem Statement: Given an array of integers nums, return the length of the longest strictly increasing subsequence. A subsequence is a sequence formed by deleting some or no elements without changing the order.

Sample: Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]

Output: 4

Explanation: The LIS is [2, 3, 7, 18], so the length is 4.

Algorithm / Approach: We use a Dynamic Programming + Binary Search approach (also known as the patience-sorting technique).

Key Idea: Maintain a list sub such that:

sub[i] = smallest possible tail value of an increasing subsequence of length i+1.


Algorithm Steps:

1. Create an empty list sub.

2. For each number x in nums: • If sub is empty or x is larger than the last element in sub, append x. • Otherwise, find the position in sub where x should go using binary search (bisect_left), and replace that element.

3. The length of sub gives the LIS length.

Why this works: We don’t store the actual LIS, but the most promising increasing subsequence tails. This ensures sub grows as slowly as possible, giving the LIS length efficiently.

Time Complexity: Best Case: O(n log n) — every number processed with binary search
Average Case: O(n log n)
Worst Case: O(n log n)

Space Complexity: Space: O(n) — we only store the potential LIS tail values in the sub list.

Example Input / Output: Input: nums = [1, 2, 4, 3]

Output: 3

Explanation: The LIS here is 1 → 2 → 3, so the length is 3.

