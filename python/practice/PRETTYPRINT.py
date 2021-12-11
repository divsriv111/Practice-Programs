import pprint
def printPattern(A):
    s = 2 * A - 1
    a = []
    for i in range(0, int(s / 2) + 1):
        m = A
        temp = []
        # Decreasing part
        for j in range(0, i):
            temp.append(m)
            m -= 1

        # Conatsant Part
        for k in range(0, s - 2 * i):
            temp.append(A-i)

            # Increasing part.
        m = A - i + 1
        for l in range(0, i):
            temp.append(m)
            m += 1
        a.append(temp)

        # Lower Half
    for i in range(int(s / 2), -1, -1):
        temp = []
        # Decreasing Part
        m = A
        for j in range(0, i):
            temp.append(m)
            m -= 1

        # Constant Part.
        for k in range(0, s - 2 * i):
            temp.append(A-i)

            # Decreasing Part
        m = A - i + 1
        for l in range(0, i):
            temp.append(m)
            m += 1
        a.append(temp)
    a.pop(A)
    return a

pprint.pprint(printPattern(4))