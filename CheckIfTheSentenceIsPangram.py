def checkIfPangram(sentence: str) -> bool:
    characterMap = {}
    for s in sentence:
        characterMap[s] = 1
    
    if len(characterMap) == 26 :
        return True
    else: 
        return False
    
print(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))



        