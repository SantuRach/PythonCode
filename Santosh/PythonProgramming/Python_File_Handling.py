'''

File Open modes:
1. read
2. write
3. append

'''


def readfile(filename):
    file = open(filename, 'r')
    data = file.read()
    print('File Content :\n', data)
    print(file.closed)
    file.close()
    print(file.closed)


#readfile('Python_File_Handling1.txt')
#readfile("c:\\pythonpractice\\pythoncode\\santosh\\questions\\clarifications.py")

def writefile(filename, content):
    file = open(filename, 'w')
    file.write(content)
    file.close()


# Method 1.
# Write to existing file. Overwrites the existing content
content = "My name is Santosh \n"
writefile('Python_File_Handling2.txt', content)

# Method 2.
# Create a new file and add the content
content = "My name is Rachotimath"
writefile('Python_File_Handling3.txt', content)


def appendfile(filename, content):
    file = open(filename, 'a')
    file.write(content)
    file.close()


content = "Surname is Rachotimath \n"
appendfile('Python_File_Handling2.txt', content)
