import os

def get_files_info(working_directory, directory=None):
    abs_working_path = os.path.abspath(working_directory)
    target_dir = abs_working_path
    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(abs_working_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        file_list = []
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename)
            file_size = 0
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            file_list.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
            return "\n".join(file_list)
    except Exception as e:
        return f"Error listing files: {e}"


