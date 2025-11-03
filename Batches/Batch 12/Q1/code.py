from bisect import bisect_left

def lengthOfLIS(nums):
    # sub will store the smallest possible tail value for all increasing subsequences 
    # of different lengths found so far
    sub = []

    for x in nums:
        # if x is greater than the last element of sub,
        # it means we have found a longer increasing subsequence
        if len(sub) == 0 or sub[-1] < x:
            sub.append(x)  # extend the subsequence
        else:
            # find the first index in sub where sub[idx] >= x
            # and replace that value with x to maintain the smallest possible tail value
            idx = bisect_left(sub, x)
            sub[idx] = x  # this keeps future subsequences more optimal

    # length of sub array = length of Longest Increasing Subsequence
    return len(sub)