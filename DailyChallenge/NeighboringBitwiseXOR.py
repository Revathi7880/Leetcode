def doesValidArrayExist(derived) -> bool:
    result = derived[0]
    for n in derived[1:]:
        result = result ^ n
    return True if result == 0 else False 

print(doesValidArrayExist([1,1,0]))