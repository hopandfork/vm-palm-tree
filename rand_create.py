import argparse

parser = argparse.ArgumentParser(description= 'This tool is intended to \
create directory & files with random contents, random (or optionally real) \
name and real extensions (by default mostly used).')

parser.add_argument('files', metavar='f', type=int, 
                   help='number of files to be generated')
parser.add_argument('--directories', metavar='d', type=int, default=0,
                   help='number of directories to be generated (default: zero)')

parser.add_argument('--real', metavar='r', 
                   help='use real name for files and directories')

parser.add_argument('--extensions', metavar='e', type=str, nargs='+',
                   default=['jpg', 'png', 'mp3', 'pdf', 'doc', 'docx', 'ppt',
                   'zip', 'avi', 'mp4'], help='type of file extensions to be \
                   generated (default=["jpg", "png", "mp3", "pdf", "doc", \
                   "docx", "ppt", "zip", "avi", "mp4"])')

parser.add_argument('--level', metavar='l', type=int, default=0,
                   help='number of nested directories to be generated (default: no nested-dir)')

parser.add_argument('--existing', metavar='x', type=bool,default=False, 
                   help='use already existing sub-directories as first nested\
                   level (default: do not use already existing sub-directories)')

parser.add_argument('path', metavar='p', type=str, 
                   help='path where create new dirs & files')

parser.add_argument('size', metavar='s', type=int, 
                   help='average size of files to be generated')

args = parser.parse_args()
print(args.accumulate(args.files))
