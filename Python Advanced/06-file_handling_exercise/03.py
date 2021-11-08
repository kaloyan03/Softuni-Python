import os

END_COMMAND = 'End'


def create_file(file_path):
    with open(f"{file_path}", 'w') as file:
        file.write('')


def add_file_content(file_path, content):
    with open(f"{file_path}", 'a') as file:
        file.write(f"{content}\n")


def replace_content(file_path, string_to_replace, new_string):
    try:
        with open(f"{file_path}", 'r+') as file:
            text = ''.join(file.readlines())
            replaced_content = text.replace(string_to_replace, new_string)
            file.seek(0)
            file.write(replaced_content)

    except FileNotFoundError:
        print(f"An error occurred")


def delete_file_path(file_path):
    try:
        os.remove(file_path)

    except FileNotFoundError:
        print("An error occurred")


mapper = {'Create': create_file,
          "Add": add_file_content,
          'Replace': replace_content,
          'Delete': delete_file_path
          }



def run_until_stop_command():
    command_data = input()
    while command_data != END_COMMAND:
        tokens = command_data.split("-")
        command, command_args = tokens[0], tokens[1:]
        mapper[command](*command_args)

        command_data = input()

run_until_stop_command()