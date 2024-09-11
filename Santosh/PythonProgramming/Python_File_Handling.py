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
    with open(filename, 'r') as file:
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
    with open(filename, 'w') as file:
        file.write(overwrite_data)


overwrite_data = "My name is Santosh & Surname is Rachotimath"
overwrite_existing_file('Python_File_Handling2.txt', overwrite_data)

####################################################################################
# program to append data to an existing file.
print("_" * 25, '# Exercise 3 #', "_" * 25)


def append_existing_file(filename, overwrite_data):
    with open(filename, 'a') as file:
        file.write(overwrite_data)


overwrite_data = "\nMy name is Santosh1 & Surname is Rachotimath1"
append_existing_file('Python_File_Handling3.txt', overwrite_data)

####################################################################################
# program to get the file’s first three and last three lines.
print("_" * 25, '# Exercise 4 #', "_" * 25)


def first_three_last_three_lines(filename):
    with open(filename, 'r') as file:
        data = file.readlines()  # loads each line of the file as one index position
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
    with open(filename, 'r') as file:
        data_list = file.readlines()  # loads each line of the file as one index position
        for i in range(len(data_list)):
            if '@' in data_list[i]:
                sub_data_list = data_list[i].split(" ")
                for j in range(len(sub_data_list)):
                    if '@' in sub_data_list[j]:
                        print(sub_data_list[j])


def get_all_the_email_ids_read(filename):
    with open(filename, 'r') as file:
        data_list = file.read()  # loads each line of the file as one index position
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
                print(data[i - 1])


num_line = 10
get_specific_line('Python_File_Handling1.txt', num_line)

####################################################################################
# file program to get odd lines from files and append them to separate files.
print("_" * 25, '# Exercise 7 #', "_" * 25)


def get_odd_line(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
        for i in range(len(data)):
            if i % 2 == 0:
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

####################################################################################
# file program to get all odd and even length words in two lists.
print("_" * 25, '# Exercise 13 #', "_" * 25)


def odd_even_len_words(filename):
    odd_len_words = []
    even_len_words = []
    with open(filename, 'r') as file:
        file_data = file.readlines()
        for i in range(len(file_data)):
            file_data_sub_list = file_data[i].split(" ")
            #print(file_data_sub_list)
            for j in range(len(file_data_sub_list)):
                if len(file_data_sub_list[j]) % 2 != 0:
                    odd_len_words.append(file_data_sub_list[j])
                else:
                    even_len_words.append(file_data_sub_list[j])
        print(odd_len_words)
        print(even_len_words)


odd_even_len_words('Python_File_Handling1.txt')

####################################################################################
# file program to get all mobile numbers from a file. e.g each mobile number size should be 10.
print("_" * 25, '# Exercise 14 #', "_" * 25)


def get_mobile_numbers1(filename):
    mobile_numbers_list = []
    with open(filename, 'r') as file:
        file_data_list = file.readlines()
        for i in range(len(file_data_list)):
            file_data_sub_list = file_data_list[i].split(" ")
            for j in range(len(file_data_sub_list)):
                if file_data_sub_list[j].isdigit() and len(file_data_sub_list[j]) == 10:
                    mobile_numbers_list.append(file_data_sub_list[j])
                else:
                    continue
        print(mobile_numbers_list)


get_mobile_numbers1('Python_File_Handling1.txt')


def get_mobile_numbers2(filename):
    mobile_numbers_list = []
    with open(filename, 'r') as file:
        file_data_list = file.read().split()
        for j in range(len(file_data_list)):
            if file_data_list[j].isdigit() and len(file_data_list[j]) == 10:
                mobile_numbers_list.append(file_data_list[j])
            else:
                continue
        print(mobile_numbers_list)


get_mobile_numbers2('Python_File_Handling1.txt')

####################################################################################
# file program to get a list of all domains from a file. e.g. .com, .au, .in
print("_" * 25, '# Exercise 15 #', "_" * 25)


def list_of_all_domains(filename):
    list_of_all_domains = []
    with open(filename, 'r') as file:
        file_data_list = file.read().split()
        for j in range(len(file_data_list)):
            if '.com' in file_data_list[j] or '.au' in file_data_list[j] or '.in' in file_data_list[j]:
                list_of_all_domains.append(file_data_list[j])
            else:
                continue
        print(list_of_all_domains)


list_of_all_domains('Python_File_Handling1.txt')

####################################################################################
# file program to get a list of all domains from a file. e.g. .com, .au, .in
print("_" * 25, '# Exercise 16 #', "_" * 25)


def list_of_all_domains(filename):
    list_of_all_domains = []
    with open(filename, 'r') as file:
        file_data_list = file.read().split()
        for j in range(len(file_data_list)):
            if '.com' in file_data_list[j] or '.au' in file_data_list[j] or '.in' in file_data_list[j]:
                list_of_all_domains.append(file_data_list[j])
            else:
                continue
        print('Is file closed ?', file.closed)
        print(list_of_all_domains)
    print('Is file closed ?', file.closed)


list_of_all_domains('Python_File_Handling1.txt')

####################################################################################
# file program to extract characters from a text file into a list.
print("_" * 25, '# Exercise 17 #', "_" * 25)


def extract_characters_list(filename):
    list_of_all_char = []
    count_upper = 0
    count_lower = 0
    count_digit = 0
    with open(filename, 'r') as file:
        file_data_list = file.read().split()
        for i in range(len(file_data_list)):
            for j in range(len(file_data_list[i])):
                list_of_all_char.append(file_data_list[i][j])
                if file_data_list[i][j].isupper():
                    count_upper += 1
                else:
                    count_lower += 1
                if file_data_list[i][j].isdigit():
                    count_digit += 1

        print(list_of_all_char)
        print(len(list_of_all_char))  # count the total number of characters in a file.
        print(count_upper)  # count the total number of Uppercase characters in a file.
        print(count_lower)  # count the total number of lowercase characters in a file.
        print(count_digit)  # count the total number of digit characters in a file.


extract_characters_list('Python_File_Handling1.txt')

####################################################################################
# file program to read the data of two of the files created and add it to a new file.
print("_" * 25, '# Exercise 18 #', "_" * 25)


def data_of_two_files_to_three(filename1, filename2, filename3):
    with open(filename1, 'r') as file1:
        file1_data = file1.read()
    with open(filename2, 'r') as file2:
        file2_data = file2.read()
    with open(filename3, 'a') as file3:
        file3.write(file1_data)
        file3.write('\n')
        file3.write(file2_data)


data_of_two_files_to_three('Python_File_Handling1.txt', 'Python_File_Handling2.txt', 'Python_File_Handling3.txt')

####################################################################################
# file program to find the cursor position in a file.
# file program to read the content of the file in reverse order..
print("_" * 25, '# Exercise 17 #', "_" * 25)


def cursor_position(filename):
    with open(filename, 'r') as file:
        file_data = file.readlines()
        for i in range(1, len(file_data) + 1):
            print(file_data[-i])
        print('Cursor position : ', file.tell())  # Print the position of the cursor
        file.seek(10)  # Moves position of the cursor to 10
        print('Cursor position : ', file.tell())  # Print the position of the cursor


cursor_position('Python_File_Handling1.txt')

####################################################################################
# file program to find the cursor position in a file.
# file program to read the content of the file in reverse order..
print("_" * 25, '# Exercise 17 #', "_" * 25)


def replace_space_by_underscore(filename):
    with open(filename, 'r') as file:
        file_data = file.read()
        print(file_data)
        file_data = file_data.replace(' ', '_')
        print(file_data)


replace_space_by_underscore('Python_File_Handling1.txt')
