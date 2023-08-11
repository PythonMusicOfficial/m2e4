import os
import json
import sys

def create_folder_and_file():
    folder_path = "C:\\Program Files\\m2e4"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    file_name = input("Enter a name for your data file: ")
    data = input("Enter your data: ")
    
    file_path = os.path.join(folder_path, f"{file_name}.json")
    with open(file_path, 'w') as file:
        json.dump(data, file)
    
    print("File created successfully!")

def choose_and_display_data():
    folder_path = "C:\\Program Files\\m2e4"
    if not os.path.exists(folder_path):
        print("There's empty. Create a new file!")
        return
    
    file_list = [f for f in os.listdir(folder_path) if f.endswith('.json')]
    
    if not file_list:
        print("There's empty. Create a new file!")
        return
    
    print("Available files:")
    for i, file in enumerate(file_list, start=1):
        print(f"{i}. {file}")
    
    choice = input("Enter the number of the file to open (or type 'exit' to quit): ")
    if choice == 'exit':
        sys.exit("Exiting the program.")
    
    try:
        choice_idx = int(choice) - 1
        chosen_file = file_list[choice_idx]
        file_path = os.path.join(folder_path, chosen_file)
        
        with open(file_path, 'r') as file:
            data = json.load(file)
            print("Data from the chosen file:")
            print(data)
    except (ValueError, IndexError):
        print("Invalid choice!")

def main():
    print("m2e4")
    action = input("Do you want to create a new file or choose an existing one? (create/choose): ")
    
    if action == "create":
        create_folder_and_file()
    elif action == "choose":
        choose_and_display_data()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
