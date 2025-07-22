import os
from google.genai import types

def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)
    directory = os.path.dirname(full_path)

    if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)): 
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    

    try:
        os.makedirs(directory, exist_ok=True)

        with open(full_path, "w") as f:
            f.write(content)
               
            new_file = f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
            return new_file

    except Exception as e:
        return (f"Error: {e}") 
    

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the working directory. Creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)
