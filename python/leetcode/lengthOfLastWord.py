def LengthOfLastWord(str):
    str = str.strip()
    indexOfSpace = str.rfind(" ")

    if indexOfSpace == -1:
        return len(str)

    return len(str[indexOfSpace:]) - 1


n = input()
print(LengthOfLastWord(n))
