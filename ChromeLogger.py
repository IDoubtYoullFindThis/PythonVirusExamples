import os
import shutil

def main():
    # Get the current user's name
    username = os.getlogin()
    
    # Construct the path to the user's directory
    user_directory = f"C:/Users/{username}/AppData/Local/Google/Chrome/User Data/Default"
    example_file_path = os.path.join(user_directory, 'Bookmarks')
    
    # Get the directory where the Python script is located
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Check if example.txt exists in the user's directory
    if os.path.exists(example_file_path):
        # Construct the destination path
        destination_path = os.path.join(script_directory, 'Bookmarks')
        
        # Copy the file to the script's directory
        shutil.copy(example_file_path, destination_path)
        print(f"File copied to {destination_path}")
    else:
        print(f"{example_file_path} does not exist.")

if __name__ == "__main__":
    main()
