def concatenate(s1: str, s2: str) -> str:
    word_length = len(s1) + len(s2)

    if word_length <= 10:
        return(s1 + s2)
    else:
        return("Too long!")


# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
