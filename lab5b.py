#!/usr/bin/env python3
# Author ID: [xli472]

def read_file_string(file_name):
    f = open(file_name, 'r')
    read_file = f.read()
    f.close()
    return read_file

def read_file_list(file_name):
    f = open(file_name, 'r')
    read_file = [line.strip() for line in f] 
    f.close()

def append_file_string(file_name, string_of_lines):
    f = open(file_name, 'a')
    read_file = f.write(string_of_lines)
    f.close() 

def write_file_list(file_name, list_of_lines):
    f = open(file_name, 'w')
    for line in list_of_lines:
        read_file = f.write(str(line) + '\n')
    f.close() 

def copy_file_add_line_numbers(file_name_read, file_name_write):
    f_read = open(file_name_read, 'r')  
    content = f_read.readlines()
    f_read.close()

    f_write = open(file_name_write, 'w')
    line_number = 1
    for lines in content:
       f_write.write(f'{line_number}: {lines}') 
       line_number += 1
    f_write.close()
 
if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
