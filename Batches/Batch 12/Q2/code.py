from bisect import bisect_left

def maxEnvelopes(envelopes):
    # Step 1: Sort envelopes
    #  - Increasing by width
    #  - If widths are same, decreasing by height (to avoid counting equal width)
    envelopes.sort(key=lambda x: (x[0], -x[1]))

    # Step 2: Extract heights (we only apply LIS on heights now)
    heights = [h for _, h in envelopes]

    # Step 3: Apply LIS on heights
    # LIS array keeps the smallest possible tail value for all increasing subsequences
    LIS = []

    for h in heights:
        # If current height is larger than the last element in LIS,
        # we can extend the sequence
        if len(LIS) == 0 or LIS[-1] < h:
            LIS.append(h)
        else:
            # Otherwise, find the position to replace using binary search
            # This ensures LIS remains optimal (smallest possible tail values)
            idx = bisect_left(LIS, h)
            LIS[idx] = h

    # The size of LIS list gives the maximum number of envelopes
    return len(LIS)