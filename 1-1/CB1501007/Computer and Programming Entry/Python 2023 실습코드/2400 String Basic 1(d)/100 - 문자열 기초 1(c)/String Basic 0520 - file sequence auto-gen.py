# 여러개의 파일을 한번에 만들어 낼 때

for fsize in range(1,31) :
    fname= "report_"+str(fsize).zfill(3)+".txt"
    print(f' fname = {fname}')
