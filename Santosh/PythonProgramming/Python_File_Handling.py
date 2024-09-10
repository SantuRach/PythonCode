"""





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

content = "Surname is Rachotimath1 \n"
appendfile('Python_File_Handling2.txt', content)

##################### Context Manager #####################
# context manager : it has it own enter and exit method, once we come out of context manager then file
# will be closed automatically

def context_manager(filename):
    with open(filename, 'r') as file:
        filedata = file.read()
        print(file.closed)
    print(file.closed)

context_manager('Python_File_Handling2.txt')

# ##################### Read methods #####################
'''
1. read specific number of bytes from file
2. read lines
3. read list of lines

'''
### read specific number of bytes from file

def read_bytes(filename, numbytes):
    with open(filename,'r') as file:
        file_data = file.read(numbytes)
        print(file_data)

num_bytes = 18
read_bytes('Python_File_Handling2.txt', num_bytes)


### read specific number of lines from file

def read_specific_lines(filename, num_lines):
    with open(filename, 'r') as file:
        for i in range(num_lines):
            print(file.readline(), end="")

num_lines = 10
read_specific_lines('Python_File_Handling2.txt', num_lines)
#

### read list of lines

def read_list_lines(filename, num_lines):
    with open(filename, 'r') as file:
        for i in range(num_lines):
            print(file.readline(), end="")

num_lines = 10
read_list_lines('Python_File_Handling2.txt', num_lines)




####################################################################################
# Program How to read a file in reading mode.
print("_" * 25, '# Exercise 1 #', "_" * 25)

def open_file_r_mode(filename):
    file = open(filename, 'r')
    data = file.read()
    print(data)
    file.close()

def open_file_r_mode_context_mgr(filename):
    with open(filename, 'r') as file:
        data = file.read()
        print(data)


open_file_r_mode('Python_File_Handling1.txt')
open_file_r_mode_context_mgr('Python_File_Handling1.txt')


####################################################################################
# program to overwrite the existing file content.
print("_" * 25, '# Exercise 2 #', "_" * 25)

def overwrite_existing_file(filename, overwrite_data):
    with open(filename,'w') as file:
        file.write(overwrite_data)

overwrite_data = "My name is Santosh & Surname is Rachotimath"
overwrite_existing_file('Python_File_Handling2.txt', overwrite_data)


####################################################################################
# program to append data to an existing file.
print("_" * 25, '# Exercise 3 #', "_" * 25)

def append_existing_file(filename, overwrite_data):
    with open(filename,'a') as file:
        file.write(overwrite_data)

overwrite_data = "\nMy name is Santosh1 & Surname is Rachotimath1"
append_existing_file('Python_File_Handling3.txt', overwrite_data)

####################################################################################
# program to get the file’s first three and last three lines.
print("_" * 25, '# Exercise 4 #', "_" * 25)

def first_three_last_three_lines(filename):
    with open(filename,'r') as file:
        data = file.readlines() # loads each line of the file as one index position
        #print(data)
        for i in data[0:3]:
            print(i)
        for i in data[-3:]:
            print(i)

first_three_last_three_lines('Python_File_Handling1.txt')


####################################################################################
# file program to get all the email ids from a text file.
print("_" * 25, '# Exercise 5 #', "_" * 25)

def get_all_the_email_ids_readlines(filename):
    with open(filename,'r') as file:
        data_list = file.readlines() # loads each line of the file as one index position
        for i in range(len(data_list)):
            if '@' in data_list[i]:
                sub_data_list = data_list[i].split(" ")
                for j in range(len(sub_data_list)):
                    if '@' in sub_data_list[j]:
                        print(sub_data_list[j])

def get_all_the_email_ids_read(filename):
    with open(filename,'r') as file:
        data_list = file.read() # loads each line of the file as one index position
        word_list = data_list.split(" ")
        for i in range(len(word_list)):
            if '@' in word_list[i]:
                print(word_list[i])

get_all_the_email_ids_readlines('Python_File_Handling1.txt')
get_all_the_email_ids_read('Python_File_Handling1.txt')


####################################################################################
# file program to get a specific line from the file.
print("_" * 25, '# Exercise 6 #', "_" * 25)

def get_specific_line(filename, num_line):
    with open(filename, 'r') as file:
        data = file.readlines()
        for i in range(len(data)):
            if i == num_line:
                print(data[i-1])


num_line = 10
get_specific_line('Python_File_Handling1.txt', num_line)

####################################################################################
# file program to get odd lines from files and append them to separate files.
print("_" * 25, '# Exercise 7 #', "_" * 25)

def get_odd_line(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
        for i in range(len(data)):
            if i%2 == 0:
                print(data[i])

get_odd_line('Python_File_Handling1.txt')

####################################################################################
# file program to find the longest word in a file.
print("_" * 25, '# Exercise 8 #', "_" * 25)

def longest_word(filename):
    max_word_length = 0
    with open(filename, 'r') as file:
        data = file.read()
        word = data.split(" ")
        for i in range(len(word)):
            if len(word[i]) >= max_word_length:
                max_word_length = len(word[i])
                max_word = word[i]
            else:
                continue
        print(max_word)


longest_word('Python_File_Handling1.txt')

####################################################################################
# file program to get the count of a specific word in a file
print("_" * 25, '# Exercise 9 #', "_" * 25)

def count_specific_word(filename):
    with open(filename, 'r') as file:
        count = 0
        data = file.read()
        word_list = data.split(" ")
        for i in range(len(word_list)):
            if word_list[i] == 'given':
                count += 1
        print(count)



count_specific_word('Python_File_Handling1.txt')

####################################################################################
# file program to get the count of a specific word in a file
print("_" * 25, '# Exercise 10 #', "_" * 25)

def count_specific_word(filename):
    with open(filename, 'r') as file:
        count = 0
        word_list = file.read().split()
        #word_list = data.split(" ")
        for i in range(len(word_list)):
            if word_list[i] == 'given':
                count += 1
        print(count)



count_specific_word('Python_File_Handling1.txt')

####################################################################################
# file program to copy the file’s contents to another file after converting it to lowercase.
print("_" * 25, '# Exercise 11 #', "_" * 25)

def copy_file_content_to_another(filename1, filename2):
    with open(filename1, 'r') as file1:
        file_data = file1.read()
        file_data_lower = file_data.lower()
        #print(file_data_upper)

    with open(filename2, 'w') as file2:
        file2.write(file_data_lower)


copy_file_content_to_another('Python_File_Handling2.txt', 'Python_File_Handling3.txt')


####################################################################################
# file file program to count all the words from a file.
print("_" * 25, '# Exercise 12 #', "_" * 25)

def copy_file_content_to_another(filename):
    with open(filename, 'r') as file:
        file_data = file.read().split()
        print(len(file_data))

copy_file_content_to_another('Python_File_Handling1.txt')



"""

####################################################################################
# file program to sort all the lines File as per line length size.
print("_" * 25, '# Exercise 12 #', "_" * 25)























