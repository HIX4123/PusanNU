

import os.path
directory = './Here/'
filename = "file.txt"
file_path = os.path.join(directory, filename)
if not os.path.isdir(directory):
    os.mkdir(directory)
file = open(file_path, "w")

for w in range(100,111) :
    #file.write( str(w) ) # file write의 argument는 반드시 string이요.
    print(f"w = {w:4}", file = file )

file.close()