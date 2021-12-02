from pprint import pprint
import os

def get_line_file(file):
    count_lines = 0
    with open(file, 'r', encoding='cp1251') as f:
        for lines in f:
            count_lines += 1
    return count_lines


def new_dict(files_dir):
    data = {}
    file_list = []
    for files in os.listdir(files_dir):
        if files.endswith(".txt"):
            file_list.append(files)
    for file in file_list:
        path_file = os.path.join(files_dir, file)
        with open(path_file, 'r', encoding='cp1251') as f:
            file_name = os.path.basename(path_file)
            file_func = (get_line_file(path_file), f.read().strip())
            data[file_name] = file_func
    return data


def sort_dict(data):
    sorted_list = sorted(data.items(), key=lambda item: item[1][0])
    sorted_dict = {k: v for k, v in sorted_list}
    with open(os.path.join('result_file', 'result.txt'), 'w', encoding='cp1251') as f:
        for k, v in sorted_dict.items():
            f.write(k + '\n')
            f.write(str(v[0]) + '\n')
            f.write(v[1] + '\n')
    return


sort_dict(new_dict('files'))