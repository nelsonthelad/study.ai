import json
import os

def save_json_to_file(json_string, filename, directory='saved'):
    os.makedirs(directory, exist_ok=True)
    
    data = json.loads(json_string)
    
    filename = filename + ".json"

    file_path = os.path.join(directory, filename)
    
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
