import os

def get_files_info(working_directory, directory=None):
    file_list = []
    abs_path = os.path.abspath(working_directory)
    subdir_path = os.path.join(abs_path, directory)
    dir_abs_path = os.path.abspath(subdir_path)
    if dir_abs_path.startswith(abs_path) == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if os.path.isdir(dir_abs_path) == False:
        return f'Error: "{directory}" is not a directory'
    files = os.listdir(dir_abs_path)
    for file in files:
        try: 
            file_path = os.path.join(dir_abs_path, file)           
        except:
            return "Error: An error occured joining file paths."
        try:
            file_size = os.path.getsize(file_path)
        except:
            return "Error: An error occured retrieving the file size."
        try:
            is_dir = os.path.isdir(file_path)
        except:
            return "Error: Unable to determine file type."
        file_string = f"- {file}: file_size={file_size} bytes, is_dir={is_dir}"
        file_list.append(file_string)
    result = "\n".join(file_list)
    return result


