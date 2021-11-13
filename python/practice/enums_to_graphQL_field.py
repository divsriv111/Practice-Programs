from sys import stdin, stdout
from pprint import pprint

#Reading from file
stdin = open('./practice/input.txt', 'r')
stdout = open('./practice/output.txt', 'w')

enums = stdin.readlines()
class_name = enums[0].replace("public enum ", "").strip()
enums[:] = enums[2:len(enums) - 1]

ans = []
stdout.writelines(f"Name = {class_name};" + '\n')
for i in enums:
    tmp = i.strip().split(' ')[0]
    ans.append(f"AddValue(\"{tmp}\", null, {class_name}.{tmp});")

for i in ans:
    stdout.writelines(i + '\n')
