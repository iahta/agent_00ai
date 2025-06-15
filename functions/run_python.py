import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    abs_working_path = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target_file):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: File "{file_path}" is not a Python file.'
    try: 
        result = subprocess.run(
            ["python3", target_file],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=os.path.dirname(target_file),
            check=True
            )
        if not result.stdout.strip() and not result.stderr.strip():
            return "No output produced."
        
        return (
            f"STDOUT: {result.stdout}\n"
            f"STDERR: {result.stderr}\n"
        )
    except subprocess.CalledProcessError:
        return f"Process exited with code {subprocess.CalledProcessError.returncode}"
    except subprocess.TimeoutExpired:
        return "Error: Script timed out after 30 seconds."
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes the selected python file with optional arguments, returns the STDOUT and STDERR, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file_path of the file to execute, within the working directory.",
                ),
            },
        ),
    )
 
    