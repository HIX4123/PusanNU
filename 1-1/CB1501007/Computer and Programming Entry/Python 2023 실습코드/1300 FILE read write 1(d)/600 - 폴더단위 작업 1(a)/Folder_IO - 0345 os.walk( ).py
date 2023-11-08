

import os
import fnmatch

dirwalk = os.walk(".")

for root, dir, files in dirwalk :
        print(root)
        print("")
        for items in fnmatch.filter(files, "*"):
                print("..." + items)
        print("")

