import os


def get_files_info(working_directory, directory=None):
    wrk_dir_abspath = os.path.abspath(working_directory)
    target_dir = wrk_dir_abspath

    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(wrk_dir_abspath):
        return f'Error: Cannot list "{directory}" as is it outside of permitted working directory!'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    try:
        files_info = []
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename)
            file_size = 0
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}")

        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"


def get_file_content(working_directory, file_path):
    wrk_dir_abspath = os .path.abspath(working_directory)
    work_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not work_file_path.startswith(wrk_dir_abspath):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(work_file_path):
        return f'Error: File not found or is not a regular file "{file_path}"'

    try:
        MAX_CHARS = 10000
        with open(work_file_path, "r") as f:
            file_content = f.read(MAX_CHARS)
            if f.read(1):
                return f"{file_content} [...File '{work_file_path}' truncated at 10000 characters]"
            return file_content
    except Exception as e:
        return f"Error cannot read file: {e}"
    

def write_file(working_directory, file_path, content):
    wrk_dir_abspath = os.path.abspath(working_directory)
    work_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not work_file_path.startswith(wrk_dir_abspath):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        with open(work_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error writing to file: {e}"
