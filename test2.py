def findLongestLength(fullString: str) -> int:
    n = len(fullString)
    # Edge case: if the string is length 1, no proper substring exists
    if n <= 1:
        return 0
    # 1) Create intervals for each distinct letter
    intervals = []
    for c in set(fullString):
        left_idx = fullString.find(c)
        right_idx = fullString.rfind(c)
        intervals.append([left_idx, right_idx])
    # 2) Sort intervals by their starting position
    intervals.sort(key=lambda x: x[0])
    
    # 3) Merge overlapping intervals
    merged = []
    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            # No overlap, start a new merged interval
            merged.append(interval)
        else:
            # Overlaps or touches, merge with the last interval
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    # 4) Find the maximum length among the merged intervals,
    #    excluding any that match the entire string [0, n-1]
    best_length = 0
    for start, end in merged:
        if start == 0 and end == n - 1:
            # This covers the entire string, so it is not a "proper" substring
            continue
        best_length = max(best_length, end - start + 1)
    return best_length


# ------------------------------
# TESTING with the sample case:
# fullString = "abadgdg"
# Expected output = 4 (either "aba" or "dgdg" -> "dgdg" is length 4).
if __name__ == "__main__":
    test_str = "amazonservices"
    print(findLongestLength(test_str))  # Should print 4
