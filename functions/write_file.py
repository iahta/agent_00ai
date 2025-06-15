import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_path = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_path):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    try:
        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        with open(target_file, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: File could not be created: "{file_path}". Reason: {e}' 
    
schema_write_file= types.FunctionDeclaration(
    name="write_file",
    description="Write or Overrite a file with the provided contents, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file_path of the file to write, within the working directory.",
                ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that will be written to the file, within the working directory.",
                ),
            },
        ),
    )