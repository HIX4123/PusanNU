#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-04-30
#-------------------------------------------------------------------------------

"""
os.exit()메서드로 Python 프로그램 종료

이 방법은 스크립트의 자식 프로세스와 같은 특별한 상태로 프로세스를
종료하는 데 사용됩니다.
os.fork()메소드를 사용하여 자식 프로세스를 생성 할 수 있습니다.
os.fork()명령은 Linux에서 효율적으로 작동합니다.
그러나 Windows 용 Cygwin을 사용해야합니다.
"""

import os

parent_id = os.fork()

if parent_id > 0:
    print("\nIn parent process")
    info = os.waitpid(parent_id, 0)
    if os.WIFEXITED(info[1]) :
        code = os.WEXITSTATUS(info[1])
        print("Child's exit code:", code)
else :
    print("child process")
    print("Process ID:", os.getpid())
    print("Test Code")
    print("Child exiting..")
    os._exit(os.EX_OK)

# os.wait()메소드는 종료 상태와 함께 하위 프로세스 ID를 반환합니다. os._exit()메소드를 사용하여 종료 코드를 얻습니다.