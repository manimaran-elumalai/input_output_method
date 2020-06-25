# filename = open("sample", 'r')
#
# for line in filename:
#     if "manimaran" in line.lower():
#         print(line, end="")
#
# filename.close()
# OR

# with open("sample", 'r') as filename:
#     for line in filename:
#         # if "manimaran" in line.lower():
#         print(line, end='')

# with open("sample", 'r') as filename:
#     line = filename.readline()
#     while line:
#         print(line, end=' ')
#         line = filename.readline()

with open("sample", 'r') as filename:
    lines = filename.readlines()
print(lines)

for line in lines:
    print(line, end='')
