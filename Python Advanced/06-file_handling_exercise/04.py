import os


def get_files_only(dir):
    files = [file for file in dir if os.path.isfile(file)]

    return files

def separate_files_extension(files):
    diff_files = {}

    for file in files:
        name, extension = os.path.splitext(file)
        if not extension in diff_files:
            diff_files[extension] = []

        diff_files[extension].append(name)
    return diff_files


def get_result(**kwargs):
    result = ''
    for extension, value in kwargs.items():
        result += f"{extension}\n"
        for name in value:
            result += f"- - - {name}{extension}\n"
    return result

local_dir = os.listdir()
files = get_files_only(local_dir)
files_dict = separate_files_extension(files)
sorted_files = dict(sorted(files_dict.items(), key= lambda x: x[0]))
result = get_result(**sorted_files)

path_to_desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop', "my_report_result.txt")
with open(path_to_desktop, 'w') as file:
    file.write(result)
