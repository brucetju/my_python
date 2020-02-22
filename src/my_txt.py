def read_txt_to_list(file_name):
    lst_lines = []
    with open(file_name,"r") as file:
        for line in file.readlines():
            line = line.strip('\n')
            lst_lines.append(line)
    return lst_lines
