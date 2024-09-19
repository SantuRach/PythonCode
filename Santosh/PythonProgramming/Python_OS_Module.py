import os
import shutil
import datetime
#
# # get current working dir
# print('-' * 50)
# dir_path = os.getcwd()
# print(dir_path)
#
# # Change current working dir
# print('-' * 50)
# os.chdir('c:\\PythonPractice\\venv\\')
# dir_path = os.getcwd()
# print(dir_path)
#
# # create directory
# print('-' * 50)
# os.mkdir('SantoshRach')
#
# # remove directory
# print('-' * 50)
# os.rmdir('SantoshRach')
#
# # remove from specific path
# print('-' * 50)
# #os.rmdir('c:\\PythonPractice\\venv\\San\\')
#
# #get list of files and folders from dir
# print('-' * 50)
# file_data = os.listdir('c:\\PythonPractice\\PythonCode\\')
# print(file_data)
#
# # join two paths and create a new path
# print('-' * 50)
# path1 = "d:\\Santosh_PC_Backup\\Python Coding\\Practice\\"
# filename1 = 'File1.txt'
#
# file_path = os.path.join(path1, filename1)
# print(file_path)
#
# ################################## Check if file exists
# print('-' * 50)
#
# file_path1 = 'd:\\Santosh_PC_Backup\\Python Coding\\Practice\\File1.txt'
# file_path2 = 'd:\\Santosh_PC_Backup\\Python Coding\\Practice\\File2.txt'
#
# print("File1 exits ?", os.path.exists(file_path1))  # True
# print("File2 exits ?", os.path.exists(file_path2))  # False
#
# ################################## Check if given path is file or folder?
# print('-' * 50)
#
# file_path1 = 'd:\\Santosh_PC_Backup\\Python Coding\\Practice\\File1.txt'
# file_path2 = 'd:\\Santosh_PC_Backup\\Python Coding\\Practice\\'
#
# print("File1 exits ?", os.path.isfile(file_path1))  # True
# print("File2 exits ?", os.path.isdir(file_path2))  # True
#
# ################################## Copy file from one location to another
# print('-' * 50)
#
# file_path1 = 'd:\\Santosh_PC_Backup\\Python Coding\\Practice\\File1.txt'
# file_path2 = 'd:\\Santosh_PC_Backup\\Python Coding\\FrontEnd\\File1.txt'
# file_path2_new1 = 'd:\\Santosh_PC_Backup\\Python Coding\\FrontEnd\\test\\File2.txt'
# file_path2_new2 = 'd:\\Santosh_PC_Backup\\Python Coding\\FrontEnd\\test\\'
#
# #os.mkdir(file_path2_new2)
#
# #shutil.copy(file_path1, file_path2)
# #shutil.copy(file_path1, file_path2_new1) #file name can be rename
#
#
# ################################## Create entire folder path
# print('-' * 50)
#
# file_path11 = 'd:\\Santosh_PC_Backup\\Python Coding\\FrontEnd\\test\\a\\s\\d\\f\\g\\'
#
# #os.makedirs(file_path11)
#
#
# ################################## Create multiple folders in same dir
# print('-' * 50)
#
# for i in range(1, 10):
#     print()
#     # os.makedirs(f'd:\\Santosh_PC_Backup\\Python Coding\\FrontEnd\\LOC{i}')
#
# ################################## get size of dir
# print('-' * 50)
# file_path1 = '"D:\\Santosh_PC_Backup\\Python Coding\\Practice1\\file1.txt"'
# # print(os.path.getsize(file_path1))
#
# ################################## get CPU count
# print('-' * 50)
# file_path11 = 'd:\\Santosh_PC_Backup\\Python Coding\\Practice\\File1.txt'
# print(os.cpu_count())
#
# ################################## Date time
# print('-' * 50)
#
# today_date = datetime.date.today()
# print(today_date)
#
# current_time_with_date = datetime.datetime.now()
# print(current_time_with_date)
#
# # date time formatting
# current_time_with_date = datetime.datetime.now()
# date_var = current_time_with_date.strftime('%d-%m-%Y-%S-%M-%H')
# print(date_var)
#
# #  Python Program To Get The Current Working Directory.
# print("_" * 25, '# Exercise 1', "_" * 25)
#
# cwd = os.getcwd()
# print(cwd)
#
# #  Python Program To Get The Environment Variable
# print("_" * 25, '# Exercise 2', "_" * 25)
#
# print(os.environ)  # prints all the env variables in the form of dict
#
# # Method 1
# print(os.getenv('ALLUSERSPROFILE'))  # prints specific env variables
#
# # Method 2
# print(os.environ['APPDATA'])  # prints specific env variables
#
# # Method 3
# print(os.environ.get('DRIVERDATA'))  # prints all the env variables in the form of dict
#
# #  Python Program To Set The Environment Variable
# print("_" * 25, '# Exercise 2', "_" * 25)
#
# # Method 1
# os.environ['Santosh1'] = 'Rachotimath1'  # prints specific env variables
# os.environ['Santosh2'] = 'Rachotimath2'  # prints specific env variables
#
# print(os.environ)
# print(os.environ.get('Santosh1'))
# print(os.getenv('Santosh1'))
#
# # Python Program To Create a Directory Using os.mkdir()
#
# dir_path = 'd:\\Santosh_PC_Backup\\Python Coding\\Practice3\\'
# dir_path = 'd:\\Santosh_PC_Backup\\Python Coding\\Practice4\\'
# # os.mkdir(dir_path)
#
# # Python Program To Create 10 directories With a Random Name.
#
# for i in range(2, 11):
#     dir_path = f'd:\\Santosh_PC_Backup\\Python Coding\\Practice{i}\\'
#     # os.mkdir(dir_path)
#
# # Python Program To Create 10 directories On a Nested Level.
# for i in range(2, 10):
#     # os.makedirs(f'd:\\Santosh_PC_Backup\\Python Coding\\Practice{i}\\1\\2\\3\\4\\5\\')
#     print()
#
# # Python Program To Remove An Empty Directory Using os.rmdir()
#
# #os.remove('d:\\Santosh_PC_Backup\\Python Coding\\Practice2\\1\\')
# #os.remove('d:\\Santosh_PC_Backup\\Python Coding\\Practice3\\1\\2\\3\\4\\')
#
# # Python Program To Join 2 paths.
#
# path1 = 'D:\\Santosh_PC_Backup\\Python Coding\\Practice1\\'
# file1 = 'file1.txt'
# path3 = os.path.join(path1, file1)
#
# print(path3)
#
# # Python Program To Check The File On a Given Path.
# path1 = 'd:\\Santosh_PC_Backup\\Python Coding\\Practice1\\file1.txt'
# path2 = 'd:\\Santosh_PC_Backup\\Python Coding\\Practice1\\file2.txt'
# print(os.path.isfile(path1))
# print(os.path.isfile(path2))
#
# # Python Program To Check The dir On a Given Path.
# path1 = 'd:\\Santosh_PC_Backup\\Python Coding\\Practice1'
# path2 = 'd:\\Santosh_PC_Backup\\Python Coding\\Practice11'
# print(os.path.isdir(path1))
# print(os.path.isdir(path2))
# #
# # Python Program To Get a list Of all data from the Target Path.
# path1 = 'd:\\Santosh_PC_Backup\\Python Coding'
# print(os.listdir(path1))
#
# # Python Program To Get The Total File Count In The Target Path.
# path1 = 'd:\\Santosh_PC_Backup\\Python Coding'
# list1 = os.listdir(path1)
# print(list1)
# file_count = folder_count = 0
# for val in list1:
#     print(val)
#     file = os.path.join(path1, val)
#     if os.path.isfile(file):
#         file_count += 1
#     elif os.path.isdir(file):
#         folder_count += 1
#     else:
#         continue
# print('File count is : ', file_count)
# print('Folder count is : ', folder_count)
#
# # Python Program To Get The Count Of Each File Extension In The Target Path.
# path1 = 'D:\\Santosh_PC_Backup\\Python Coding\\Practice1\\'
# list1 = os.listdir(path1)
# final_list = []
# for val in list1:
#     val_list = val.split('.')
#     final_list.append(val_list[-1])
#
# print('File count is : ', final_list.count('txt'))
# print('json count is : ', final_list.count('json'))
# print('py count is : ', final_list.count('py'))
#
# # Python Program To Copy The File Source Path To The Target Path.
#
# path1 = 'D:\\Santosh_PC_Backup\\Python Coding\\Practice1\\file1.txt'
# path2 = 'D:\\Santosh_PC_Backup\\Python Coding\\Practice2\\file2.txt'
#
# shutil.copy(path1, path2)
#
# # Python Program To Copy Specific Extension Files From The Source To The Target Path.
#
# path1 = 'D:\\Santosh_PC_Backup\\Python Coding\\Practice1\\'
# path2 = 'D:\\Santosh_PC_Backup\\Python Coding\\Practice2\\'
#
# list_files = os.listdir(path1)
# print(list_files)
# for file in list_files:
#     if '.txt' in file:
#         path3 = os.path.join(path1,file)
#         shutil.copy(path3, path2)
#
# # Python Program To Copy 10 Files In 10 Different Nested Directories.
# path1 = 'D:\\Santosh_PC_Backup\\Python Coding\\Practice2\\'
# list_files = os.listdir(path1)
# for i in range(len(list_files)):
#     src_path = os.path.join(path1, list_files[i])
#     os.mkdir(f'D:\\Santosh_PC_Backup\\Python Coding\\Practice2\\file{i}')
#     dest_path = os.path.join(path1, f'file{i}')
#     shutil.copy(src_path, dest_path)
#
# # Python Program To Remove The File From The Given Path.
# path1 = 'D:\\Santosh_PC_Backup\\Python Coding\\Practice2\\file1 - Copy (4) - Copy.txt'
#
# #os.remove(path1)
#
# # Python Program To remove Specific Extension Files From The Target Path.
# path1 = 'D:\\Santosh_PC_Backup\\Python Coding\\Practice2\\'
#
# list_files = os.listdir(path1)
# for file in list_files:
#     if '.txt' in file:
#         rem_file = os.path.join(path1, file)
#         os.remove(rem_file)

# Write a Python Program To Create a Backup Application.
# Note: We have To filter each extension file and copy it To a specific folder.
path1 = 'D:\\Santosh_PC_Backup\\Python Coding\\Practice1\\'














