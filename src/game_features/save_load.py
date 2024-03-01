import os
import json


def save_file_with_numbered_suffix(folder_path:str, file_name:str, file_content:str, file_ext='json'):
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    new_file_path = os.path.join(folder_path, f"{file_name}.{file_ext}")
    
    with open(new_file_path, "w") as f:
        # Write content to the file if needed
        f.write(file_content)

    print(f"File saved: {new_file_path}")


def save_chat(folder_path:str, file_name:str, chat:list):
    save_file_with_numbered_suffix(
        folder_path,
        file_name,
        json.dumps(chat)
    )


def load_json_file_from_folder(folder_path:str, file_name:str, file_number:int):
    
    file = f"{file_name}_{file_number}.json"
    # Construct the full path to the JSON file
    file_path = os.path.join(folder_path, file)

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"File {file} not found in folder {folder_path}")
        return None

    # Load and parse the JSON data
    with open(file_path, "r") as f:
        try:
            data = json.load(f)
            return data
        except json.JSONDecodeError:
            print(f"Error decoding JSON file: {file_name}")
            return None

def save(chat:list):
    FOLDER = './transcripts'
    file = input("Write a name for your game: ")
    save_chat(FOLDER, file, chat)