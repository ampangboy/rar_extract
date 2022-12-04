import os
import patoolib

inp_directory = input("Directory to extract?\n")

if not os.path.isdir(inp_directory):
    print('not dir')

for (root, dirs, file) in os.walk(inp_directory):
    for f in file:
        if os.path.splitext(f)[1] == ".rar":
            fullpath = os.path.join(root, f)

            patoolib.extract_archive(fullpath, outdir=root)

            os.remove(fullpath)


