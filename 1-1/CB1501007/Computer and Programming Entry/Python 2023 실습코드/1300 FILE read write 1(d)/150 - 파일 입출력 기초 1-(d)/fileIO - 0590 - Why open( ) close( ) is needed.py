


myfile = open("noclose.txt" ,"w")


myfile.write("메롱")
myfile.write("찌롱")
myfile.write("뽀롱\n")
myfile.write("꼬롱")
print("1", file=myfile)
print("2", file=myfile)
print("3", file=myfile)  #메모리에서만 동작.


myfile.close()   # 최종적으로 disk에 file로 쓰기

