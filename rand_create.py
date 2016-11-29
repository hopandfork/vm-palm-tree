from pathlib import Path
import os
import argparse
import random
import string


# Useful override so that treats each space-separated word as an argument. 
def convert_arg_line_to_args(self, arg_line):
    return arg_line.split()


'''Create around size bytes of garbage'''
def create_garbage(size):
    approx = int(size/1000)
    max = random.randint(size - approx,size + approx)
    chapter = ''.join(random.choice(string.printable) for _ in range(0, max))
    return chapter


'''Create a random name for a directory'''
def create_dname():
    max = random.randint(3, 20)
    name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(0, max))
    return name


'''Create a random name for a file'''
def create_fname(ext):
    max = random.randint(3, 50)
    name = ''.join(random.choice(string.ascii_letters + ' ' + string.digits) for _ in range(0, max)).strip() + '.' + ext
    return name


'''Create a single file on a given path'''
def create_file(size, exts, path):
    f_name = create_fname(exts)
    f = open(os.path.join(path, f_name), 'w')
    f.write(create_garbage(size))
    f.close()


'''Create files on a set of dirs'''
def create_files(n, size, exts, paths):
    files_for_dir = int(n / len(paths))
    for dir in paths:
        for file in range(0, files_for_dir):
            create_file(size, random.choice(exts), dir)


'''Create sub-directories'''
def create_subdirs(dirs, curr_path):
    new_dirs = []
    for dir in range(0, dirs):
        d_name= create_dname()
        current_path = os.path.join(curr_path, d_name)
        Path(current_path).mkdir()
        #files_for_subdir = int(n/dirs)
        #create_files(files_for_subdir, size, exts, current_path)
        new_dirs.append(current_path)
    return new_dirs


def main(args):
    #Just a toy.
    print(args)
    
    if Path(args.path).is_dir() is False:
        Path(args.path).mkdir()
    path = args.path
    sub_dirs = []
    if args.existing:
        for entry in os.listdir(path):
            sub_dirs.append(os.path.join(path, entry))
    if args.directories != 0:
        sub_dirs.extend(create_subdirs(args.directories, path))
    if len(sub_dirs) == 0:      #use root path ONLY if no other dirs are used
        sub_dirs.append(path)
        
    create_files(args.files, args.size, args.ext_list, sub_dirs)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= 'This tool is intended to \
    create directory & files with random contents, random (or optionally real) \
    name and real extensions (by default mostly used).')

    group = parser.add_mutually_exclusive_group()

    parser.add_argument('files', metavar= 'N', type=int,  
                       help='number of files to be generated')

    parser.add_argument('-d', '--directories', metavar='M', type=int, default=0,
                       help='number of directories to be generated (default: zero)')

    parser.add_argument('-r', '--real', action='store_true',
                       help='use real name for files and directories')

    group.add_argument('--ext-file', metavar='filename', type=str,
                       help='file containing a list of type of file extensions to be \
                       generated')

    group.add_argument('--ext-list', metavar=('pdf', 'doc'), type=str, nargs='+',
                       default=['jpg', 'png', 'mp3', 'pdf', 'doc', 'docx', 'ppt',
                       'zip', 'avi', 'mp4'], help='type of file extensions to be \
                       generated (default=["jpg", "png", "mp3", "pdf", "doc", \
                       "docx", "ppt", "zip", "avi", "mp4"])')

    parser.add_argument('-l', '--level', type=int, default=0,
                        help='number of nested directories to be generated \
                        (default: no nested-dir)')

    parser.add_argument('-e', '--existing', action='store_true',
                        help='use already existing sub-directories as first nested\
                        level (default: do not use already existing \
                        sub-directories)')

    parser.add_argument('path', type=str, 
                        help='path where create new dirs & files')

    parser.add_argument('size', type=int, 
                        help='average size of files to be generated in bytes')

    args = parser.parse_args()
    main(args)
