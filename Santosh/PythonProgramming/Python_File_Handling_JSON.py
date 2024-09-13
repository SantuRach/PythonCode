import json

def read_json_data(filename):
    with open(filename, 'r') as file:
        data = file.read()
        json_data = json.loads(data)
        print(json_data)
        print(json_data['Surname'])
        print(json_data['Phone'])
        print(json_data['Country'])
        print(json_data['test_data'])
        print(json_data['test_data']['test_01'])
        print(json_data['test_data']['test_01']['username'])
        print(json_data['test_data']['test_01']['password'])

read_json_data('Python_File_Handling1.json')
