def stringMatching(words):
    substring = []
    n = len(words)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if words[i] in words[j]:
                substring.append(words[i])
                break
    return substring

print(stringMatching(["mass","as","hero","superhero"]))

    