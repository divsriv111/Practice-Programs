def strStr(haystack: str, needle: str) -> int:
        if haystack == needle or needle == "":
            return 0
        
        if len(needle) > len(haystack):
            return -1
        
        for i in range(len(haystack)):
            if needle[0] == haystack[i]:
                index = i
                pos = 0
                while pos != len(needle):
                    if haystack[i + pos] != needle[pos]:
                        break
                    pos += 1
                if pos == len(needle):
                    return index
        return -1

print(strStr("mississippi", "issip"))
