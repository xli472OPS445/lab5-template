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
    return read_file

if __name__ == '__main__':
    file_name = '/home/xli472/ops445/lab5-template/data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
