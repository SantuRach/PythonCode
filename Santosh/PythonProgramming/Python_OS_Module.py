import os
import shutil
import datetime

# get current working dir
print('-'*50)
dir_path = os.getcwd()
print(dir_path)

# Change current working dir
print('-'*50)
os.chdir('c:\\PythonPractice\\venv\\')
dir_path = os.getcwd()
print(dir_path)

# create directory
print('-'*50)
os.mkdir('SantoshRach')

# remove directory
print('-'*50)
os.rmdir('SantoshRach')

# remove from specific path
print('-'*50)
#os.rmdir('c:\\PythonPractice\\venv\\San\\')

#get list of files and folders from dir
print('-'*50)
file_data = os.listdir('c:\\PythonPractice\\PythonCode\\')
print(file_data)

# join two paths and create a new path
print('-'*50)
path1 = "d:\\Santosh_PC_Backup\\Python Coding\\Practice\\"
filename1 = 'File1.txt'

file_path = os.path.join(path1, filename1)
print(file_path)

################################## Check if file exists
print('-'*50)

file_path1 = 'd:\\Santosh_PC_Backup\\Python Coding\\Practice\\File1.txt'
file_path2 = 'd:\\Santosh_PC_Backup\\Python Coding\\Practice\\File2.txt'

print("File1 exits ?", os.path.exists(file_path1)) # True
print("File2 exits ?", os.path.exists(file_path2)) # False

################################## Check if given path is file or folder?
print('-'*50)

file_path1 = 'd:\\Santosh_PC_Backup\\Python Coding\\Practice\\File1.txt'
file_path2 = 'd:\\Santosh_PC_Backup\\Python Coding\\Practice\\'

print("File1 exits ?", os.path.isfile(file_path1)) # True
print("File2 exits ?", os.path.isdir(file_path2)) # True

################################## Copy file from one location to another
print('-'*50)

file_path1 = 'd:\\Santosh_PC_Backup\\Python Coding\\Practice\\File1.txt'
file_path2 = 'd:\\Santosh_PC_Backup\\Python Coding\\FrontEnd\\File1.txt'
file_path2_new1 = 'd:\\Santosh_PC_Backup\\Python Coding\\FrontEnd\\test\\File2.txt'
file_path2_new2 = 'd:\\Santosh_PC_Backup\\Python Coding\\FrontEnd\\test\\'

#os.mkdir(file_path2_new2)

#shutil.copy(file_path1, file_path2)
#shutil.copy(file_path1, file_path2_new1) #file name can be rename


################################## Create entire folder path
print('-'*50)

file_path11 = 'd:\\Santosh_PC_Backup\\Python Coding\\FrontEnd\\test\\a\\s\\d\\f\\g\\'

#os.makedirs(file_path11)


################################## Create multiple folders in same dir
print('-'*50)

for i in range(1, 10):
    print()
    # os.makedirs(f'd:\\Santosh_PC_Backup\\Python Coding\\FrontEnd\\LOC{i}')



################################## get size of dir
print('-'*50)
file_path11 = 'd:\\Santosh_PC_Backup\\Python Coding\\Practice\\File1.txt'
print(os.path.getsize(file_path11))


################################## get CPU count
print('-'*50)
file_path11 = 'd:\\Santosh_PC_Backup\\Python Coding\\Practice\\File1.txt'
print(os.cpu_count())


################################## Date time
print('-'*50)

today_date = datetime.date.today()
print(today_date)


current_time_with_date = datetime.datetime.now()
print(current_time_with_date)


# date time formatting
current_time_with_date = datetime.datetime.now()
date_var = current_time_with_date.strftime('%d-%m-%Y-%S-%M-%H')
print(date_var)




################################## Date time
print('-'*50)
