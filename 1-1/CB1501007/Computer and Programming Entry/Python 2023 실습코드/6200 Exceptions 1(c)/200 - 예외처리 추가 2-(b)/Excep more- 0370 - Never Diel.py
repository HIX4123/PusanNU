

# 시스템에서 control-C는 가장 강력한 interrupt이다.
# 이걸 사용하면 대부분 시스템에서는 다 죽는다.

import sys
import time

while( True ) :
    print("It's running")
    time.sleep(1)  # 1초간 뒨다.
