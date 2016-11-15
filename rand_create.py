import argparse

# Useful override so that treats each space-separated word as an argument. 
def convert_arg_line_to_args(self, arg_line):
    return arg_line.split()

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
                   help='filename of a list of type of file extensions to be \
                   generated')

group.add_argument('--ext-list', metavar=('pdf', 'doc'), type=str, nargs='+',
                   default=['jpg', 'png', 'mp3', 'pdf', 'doc', 'docx', 'ppt',
                   'zip', 'avi', 'mp4'], help='type of file extensions to be \
                   generated (default=["jpg", "png", "mp3", "pdf", "doc", \
                   "docx", "ppt", "zip", "avi", "mp4"])')

parser.add_argument('-l', '--level', type=int, default=0,
                   help='number of nested directories to be generated (default: no nested-dir)')

parser.add_argument('-e', '--existing', 
                   help='use already existing sub-directories as first nested\
                   level (default: do not use already existing sub-directories)')

parser.add_argument('path', type=str, 
                   help='path where create new dirs & files')

parser.add_argument('size', type=float, 
                   help='average size of files to be generated in MB')

args = parser.parse_args()
#Just a toy.
print(args)
