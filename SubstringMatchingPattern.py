def hasMatch(s: str, p: str) -> bool:
    left, _, right = p.partition('*')
    start_idx = s.find(left)
    print(start_idx)
    while start_idx != -1:
        if right in s[start_idx + len(left):]:
            return True
        start_idx = s.find(left, start_idx + 1)
    return False

print(hasMatch("leetcode", "ee*e"))