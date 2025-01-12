def findLongestLength(fullString: str) -> int:
    n = len(fullString)
    if n <= 1:
        # If length is 1, there's no proper substring at all
        return 0
    from string import ascii_lowercase
    leftMost = {c: -1 for c in ascii_lowercase}
    rightMost = {c: -1 for c in ascii_lowercase}
    
    for i, ch in enumerate(fullString):
        if leftMost[ch] == -1:
            leftMost[ch] = i
        rightMost[ch] = i 
    best_length = 0
    # Enumerate all substrings (start..end)
    for start in range(n):
        for end in range(start, n):
            length = end - start + 1

            if length == n:
                continue
            sub_chars = set(fullString[start:end+1])

            is_valid = True
            for c in sub_chars:
                if leftMost[c] == -1:
                    continue
                if leftMost[c] < start or rightMost[c] > end:
                    is_valid = False
                    break            
            if is_valid and length > best_length:
                best_length = length
    return best_length

# ----------------------------------------------------------------------
# Quick tests on the examples:
if __name__ == "__main__":
    # 1) Example: "abadgdg"
    # Proper self-sufficient substrings: "aba" -> length 3, "dgdg" -> length 4
    # Expect 4
    print(findLongestLength("abadgdg"))  # Should be 4
    
    # 2) Example: "amazonservices" (length=14)
    # The longest self-sufficient proper substring is "zonservices" -> length 11
    # Expect 11
    print(findLongestLength("amazonservices"))  # Should be 11
