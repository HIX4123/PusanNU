tnumber = 130
tstring = "summer"
tlist   = [3,4,5,6,7]
ttuple  = (3,4,5)
tdict   = {"beer":3500, "soju":1700}


print(tnumber, tstring, tlist, ttuple, tdict)

fnumber = 0
fstring = ""
flist   = []
ftuple  = ()
fdict   = {}


print(fnumber, fstring, flist, ftuple, fdict)


if ( not fstring ) : print("fstring은 빈 문자열입니다")
if ( not flist   ) : print("fslist는  빈 리스트입니다")
if ( not ftuple  ) : print("ftuple는  빈 튜플입니다")
if ( not fdict   ) : print("fdict는  빈 딕셔너리입니다")