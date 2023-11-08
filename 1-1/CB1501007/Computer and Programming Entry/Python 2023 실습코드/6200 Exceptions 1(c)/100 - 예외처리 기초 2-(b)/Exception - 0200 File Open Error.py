
import sys

try:
    f = open('myfile.txt') #파일 오픈에러 시 IOError가 발생
    s = f.readline()
    i = int(s.strip())         #int type으로 변불가 시 ValueError 발생

except IOError as err:   #IOError 발생 시 처리
    print(("I/O error: {0}".format(err)))

except ValueError:        #ValueError 발생 시 처리
    print("Could not convert data to an integer.")

except:                        #그 외 에러시 처리
    print(("Unexpected error:", sys.exc_info()[0]))
    raise
