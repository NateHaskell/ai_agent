import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)

    if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)): 
        return f'Error: cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    
    
    try:
        directory_contents = os.listdir(full_path)

        lines = []
        for item in directory_contents:
            lines.append(f"- {item}: file_size={os.path.getsize(os.path.join(full_path, item))} bytes, is_dir={os.path.isdir(os.path.join(full_path, item))}")
    
        return "\n".join(lines)
    
    except Exception as e:
        return (f"Error: {e}")
