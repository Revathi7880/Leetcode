def lengthOfLastWord(s: str) -> int:
    wordCount = 0
    for i in reversed(s):
        if i == ' ' and wordCount > 0:
            return wordCount
        elif i == ' ' and wordCount == 0:
            continue
        else:
            wordCount += 1
    return wordCount

print(lengthOfLastWord("   fly me   to   the moon  "))