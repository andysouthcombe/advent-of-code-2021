def read_one_line_int_file(filename):
    with open(filename,'r') as f:
        line = f.read().rstrip()
        return [int(num) for num in line.split(',')]

def read_file_of_strings(filename):
    with open(filename,'r') as f:
        return [line.rstrip() for  line in f]