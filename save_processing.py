import json
import os

def save_json_to_file(json_string, filename, directory='saved'):
    os.makedirs(directory, exist_ok=True)
    
    data = json.loads(json_string)
    
    filename = filename + ".json"

    file_path = os.path.join(directory, filename)
    
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def update_best_score(filename, score):
    file_path = os.path.join('saved', filename + ".json")
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    previous_score = data['metadata']['best_score']
    new_score = score

    if previous_score == "N/A" or get_correct_q_num(new_score) > get_correct_q_num(previous_score):
        print("Updating Best Score...")
        data['metadata']['best_score'] = new_score
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

def get_file_data(file):
        file_path = os.path.join("saved", f"{file}.json")
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return json.load(f)
        return None

def get_correct_q_num(score):
    correct = 0
    for i in range(len(score)):
        if score[i] == "Correct!":
            correct += 1
    return correct

def update_attemtps(file):
    print("Updating Attempts...")
    data = get_file_data(file)

    data['metadata']['attempts'] += 1
    file_path = os.path.join('saved', file + ".json")
    with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

          
