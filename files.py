import os

f = open('notes.txt', 'r')
# print(f.readline())

# for line in f:
#     print(line)

try:
    print(f.read())
except Exception as e:
    print(f"Error: {e}")
finally:
    f.close()

# append - creates the file if it doesn't exists
f = open('notes.txt', 'a')
f.write('\nThis is a new line')
f.close()


f = open('notes.txt')
print(f.read())
f.close()

# write - overwrites the file
f = open('context.txt', 'w')
f.write('\nThis is a new line that overwrites the file')
f.close()

f = open('context.txt')
print(f.read())
f.close()


# Oepns a file for writing and creates the file if it doesn't exist
# f = open('conjo.txt', 'x')
# # f.write('\nThis is a new line that overwrites the file')
# f.close()

# if not os.path.exists('names_list.txt'):
#     f = open('names_list.txt', 'x')
#     f.close()

# avoid an error if file exists
if os.path.exists('names_list.txt'):
    os.remove('names_list.txt')
else:
    print('File does not exist')