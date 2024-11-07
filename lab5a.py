#!/usr/bin/env python3
# Author ID: [xli472]

def read_file_string(file_name):
    f = open('file_name', 'w')
    for name in f:
        f.write(str(f) + '\n')
    f.close() 

def read_file_list(file_name):
    file_name = open('file_name', 'w')
    for name in file_name:
        file_name.write(str(file_name) + '\n')
    file_name.close() 

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
