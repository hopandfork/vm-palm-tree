from pathlib import Path
import os
import argparse
import random
import string


# Useful override so that treats each space-separated word as an argument. 
def convert_arg_line_to_args(self, arg_line):
    return arg_line.split()


def create_garbage():
    max = random.randint(1000,1500)
    chapter = ''.join(random.choice(string.printable) for _ in range(0, max))
    return chapter

def create_dname():
    max = random.randint(3, 20)
    name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(0, max))
    return name


def create_fname(ext):
    max = random.randint(3, 50)
    name = ''.join(random.choice(string.ascii_letters + ' ' + string.digits) for _ in range(0, max)).strip() + '.' + random.choice(ext)
    return name


def create_files(n, size, exts, curr_path):
    for file in range(0, n):
        f_name = create_fname(exts)
        f = open(os.path.join(curr_path, f_name), 'w')
        curr_size = 0
        while curr_size < size: 
            f.write(create_garbage())
            curr_size = f.tell()
        f.close()


def create_subdirs(dirs, n, size, exts, curr_path):
    for dir in range(0, dirs):
        d_name= create_dname()
        current_path = os.path.join(curr_path, d_name)
        Path(current_path).mkdir()
        files_for_subdir = int(n/dirs)
        create_files(files_for_subdir, size, exts, current_path)


def main(args):
    #Just a toy.
    print(args)
    
    if Path(args.path).is_dir() is False:
        Path(args.path).mkdir()
    path = args.path

    if args.directories == 0:
        create_files(args.files, args.size, args.ext_list, path)
    else:
        create_subdirs(args.directories, args.files, args.size, args.ext_list, path)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= 'This tool is intended to \
    create directory & files with random contents, random (or optionally real) \
    name and real extensions (by default mostly used).')

    group = parser.add_mutually_exclusive_group()

    parser.add_argument('files', metavar= 'N', type=int,  
                       help='number of files to be generated')

    parser.add_argument('-d', '--directories', metavar='M', type=int, default=0,
                       help='number of directories to be generated (default: zero)')

    parser.add_argument('-r', '--real', 
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

    parser.add_argument('-e', '--existing', 
                        help='use already existing sub-directories as first nested\
                        level (default: do not use already existing \
                        sub-directories)')

    parser.add_argument('path', type=str, 
                        help='path where create new dirs & files')

    parser.add_argument('size', type=float, 
                        help='average size of files to be generated in MB')

    args = parser.parse_args()
    main(args)
