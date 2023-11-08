#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-11-16
#-------------------------------------------------------------------------------

#
# If the reason you're checking is so you can do something like if file_exists:
# open_it(), it's safer to use a try around the attempt to open it.
# Checking and then opening risks the file being deleted or moved or something
# between when you check and when you try to open it.
#
# If you're not planning to open the file immediately,
# you can use os.path.isfile
#
# Return True if path is an existing regular file.
# This follows symbolic links, so both islink() and isfile() can be true
# for the same path.

import os.path
os.path.isfile(fname)

# 파일이 존재하는지의 여부를 확인하는 방법
# Python 3.4 이상부터는 pathlib 을 제공한다.

from pathlib import Path

my_file = Path("/path/to/file")
if my_file.is_file():   # file exists
else print( "my_file이 존재하지 않습니다.")

# Return True if path is an existing regular file.
# This follows symbolic links, so both islink() and isfile() can be true
# for the same path.

import os.path
os.path.isfile(fname)


from pathlib import Path

my_file = Path("/path/to/file")
if my_file.is_file():
    # file exists


if my_file.is_dir():     # directory exists
    print( "Yes 디럭토리가 존재함.")

if my_file.exists():     # path exists
    print( "Yes path가 존재함.")


try:
    my_abs_path = my_file.resolve(strict=True)
except FileNotFoundError:     # doesn't exist
else: print( "Yes")     # exists