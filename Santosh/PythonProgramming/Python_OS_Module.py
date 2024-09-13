import os

# get current working dir
dir_path = os.getcwd()
print(dir_path)

# Change current working dir
os.chdir('c:\\PythonPractice\\venv\\')
dir_path = os.getcwd()
print(dir_path)

# create directory
os.mkdir('SantoshRach')

# remove directory
os.rmdir('SantoshRach')

# remove from specific path
#os.rmdir('c:\\PythonPractice\\venv\\San\\')

#get list of files and folders from dir

file_data = os.listdir('c:\\PythonPractice\\PythonCode\\')
print(file_data)