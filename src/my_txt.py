def read_txt_to_list(file_name):
    lst_lines = []
    with open(file_name,"r") as file:
        for line in file.readlines():
            line = line.strip('\n')
            lst_lines.append(line)
    return lst_lines


def write_list_to_txt(lst_lines,file_name):
    with open(file_name,"w") as file:
        for line in lst_lines:
            file.write(line)
            file.write("\n")
