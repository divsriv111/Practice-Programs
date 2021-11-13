from sys import stdin, stdout

#Reading from file
stdin = open('./practice/input.txt', 'r')
stdout = open('./practice/output.txt', 'w')

#cleaning and standizing
props = stdin.readlines()
props = [x.replace(".cs", "").strip() for x in props]

for i in props:
    stdout.writelines(f"services.AddSingleton<{i}>();\n")