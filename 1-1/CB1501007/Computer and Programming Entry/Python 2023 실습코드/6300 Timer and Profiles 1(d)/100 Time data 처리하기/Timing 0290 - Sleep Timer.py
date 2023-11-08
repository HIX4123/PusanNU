
N = 10
import time
import threading

class Timer(threading.Thread):
  def __init__(self, seconds):
      self.runTime = seconds
      threading.Thread.__init__(self)

  def run(self):
    print("자 이제 N초 동안 sleep합니다.")
    time.sleep(self.runTime)
    print("Buzzzz!! Time's up!")
    print("알람이 울립니다.", N)

print("우리는", N, "초를 설정합니다 ")
t = Timer( N )
t.run()

print("After %d , Alarm worked! You got this" % N)

