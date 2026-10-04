def remove_fourth_character(word: str) -> str:
    b = word[:3]
    a = word[4:]
    
    return b + a


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
