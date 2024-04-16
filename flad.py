import os


def generate_directory_structure(startpath):

    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)

        indent = ' ' * 4 * level
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for file in files:
            print('{}{}'.format(subindent, file))


generate_directory_structure('api')
