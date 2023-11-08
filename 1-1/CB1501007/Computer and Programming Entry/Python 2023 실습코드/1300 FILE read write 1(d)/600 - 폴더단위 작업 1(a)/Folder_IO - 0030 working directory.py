#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-07-27
#-------------------------------------------------------------------------------

#

import os


print("\n 현재 Working Directory: " , os.getcwd())

os.chdir( 'data')
print("\n 현재 Working Directory: " , os.getcwd())


try: # Change the current working Directory
    new_path = "/home/varun/temp"
    os.chdir( new_path )
    print("Directory changed")
except OSError:
    print(f"Can't change to {new_path}: ")


if os.path.exists("/home/varun/temp") : # Change the current working Directory
    os.chdir("/home/varun/temp")
else:
    print("Can't change the Current Working Directory")


print("Current Working Directory " , os.getcwd())





