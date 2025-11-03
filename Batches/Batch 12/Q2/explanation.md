Russian Doll Envelopes (Max Envelopes):

Problem Statement: Given a list of envelopes where each envelope is represented as [width, height], determine the maximum number of envelopes that can be nested (one inside another). An envelope can fit into another only if both its width and height are strictly smaller.

Sample: Input:

envelopes = [[5,4],[6,4],[6,7],[2,3]]

Output:

3

Explanation: The sequence of envelopes that can be nested is:
[2,3] → [5,4] → [6,7]
So the maximum number is 3.

Algorithm / Approach: We convert this problem into a Longest Increasing Subsequence (LIS) problem on heights.

Steps:

1. Sort envelopes:

Ascending by width

Descending by height when widths are equal
(prevents invalid LIS when widths are same)

2. Extract the heights.

3. Apply LIS (with binary search) on the heights to get the longest increasing chain.

Why this works: Sorting by width ensures increasing width order. Sorting heights in reverse when widths are equal prevents same-width envelopes from being incorrectly counted in LIS.

Then we find the LIS on heights, which gives the maximum chain of envelopes that can fit inside each other.

Time Complexity:

O(n log n) — each height processed with binary search


Space Complexity:

O(n) — LIS list storage


Example Input / Output: Input:

[[1,1],[2,2],[3,3]]

Output:

3

Explanation: Each envelope can fit into the next, so answer = 3.