from sys import stdin, stdout
from pprint import pprint

#Reading from file
stdin = open('./practice/input.txt', 'r')
stdout = open('./practice/output.txt', 'w')

#cleaning and standizing
props = stdin.readlines()
for index, item in enumerate(props):
    tmp = item.replace("public ", "").strip()
    prop_datatype = tmp[:tmp.index(' ')]
    tmp = tmp[tmp.index(' '):].strip()
    prop_name = ''
    if tmp.__contains__(' '):
        prop_name = tmp[:tmp.index(' ')]
    else:
        prop_name = tmp[:tmp.index('\n')]
    props[index] = f"{prop_datatype} {prop_name}"
    # print(props[index])

#defining what we know in datatypes
datatypes = [
    "int?", "int", "string", "double", "double?", "float", "float?", "bool",
    "bool?", "decimal", "decimal?", "DateTime?", "DateTime", "long", "long?"
]

#processing
included = []
for i in props:
    s = ''
    tmp = i.strip().split(' ')
    if tmp[0] not in datatypes:
        if tmp[0].__contains__("IEnumerable"):
            tmp2 = tmp[0].split('<')[1].replace('>', '')
            s = s = f'Field(p => p.{tmp[1]}, true, typeof(ListGraphType<{tmp2}Type>));'
        else:
            tmp[1] = tmp[1].replace('>', '')
            s = s = f'Field(p => p.{tmp[1]}, true, typeof({tmp[1]}Type));'
    elif i.__contains__('string') or i.__contains__('?'):
        s = f'Field(p => p.{tmp[1]}, true);'

    else:
        s = f'Field(p => p.{tmp[1]});'
    included.append(s)

if len(props) != len(included):
    print("WARN: Some properties are missing!!")

#finally writing into the file
for i in included:
    stdout.writelines(i + '\n')
