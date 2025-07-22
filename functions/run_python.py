import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.join(working_directory, file_path)
    

    if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)): 
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    
    if not full_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:

        completed_process = subprocess.run(
            ["python", file_path] + args, 
            timeout=30,
            capture_output=True,
            cwd=working_directory,
            text=True
        )  

        if not completed_process.stdout.strip() and not completed_process.stderr.strip():
            return "No output produced."
        
        output = f'STDOUT: {completed_process.stdout}STDERR: {completed_process.stderr}'

        if completed_process.returncode != 0:
            output += f'Process exited with code {completed_process.returncode}'
        
        return output

        

    except Exception as e:
        return (f"Error: executing Python file: {e}") 
    

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)
    