def prefixCount(words, pref: str) -> int:
    count = 0
    for w in words:
        if w.startswith(pref):
            count += 1
    return count

print(prefixCount(["pay","attention","practice","attend"], "at"))