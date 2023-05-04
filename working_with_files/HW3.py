import os


def data_files_in_folder(folder: str) -> dict:
    path = os.path.join(os.getcwd(), folder)
    res = {}
    for filename in os.listdir(path):
        full_path = os.path.join(path, filename)
        if os.path.isfile(full_path):
            with open(full_path, 'r', encoding='utf-8') as file:
                data = file.readlines()
                res[len(data), filename] = data
    return res


def write_to_new_file(filename: str) -> None:
    with open(filename, 'w', encoding='utf-8') as new_file:
        folder = 'files'
        for key, value in sorted(data_files_in_folder(folder).items()):
            new_file.write(f'{key[1]}\n')
            new_file.write(f'{key[0]}\n')
            new_file.writelines(value)
            new_file.write('\n')


if __name__ == '__main__':
    write_to_new_file('new_file.txt')
