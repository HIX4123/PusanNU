
import re # regular expression

astr  = 'Beautiful, is; bet\ter*than\nugly'
alist = re.split('; | |,|\*|\n', astr )
print(alist)

s = "one two 3.4 5,6 seven.eight nine,ten"
blist = re.split('\s|(?<!\d)[,.](?!\d)', s)
print(blist)

cstr="무궁화 꽃이 피었습니다.아름답게 피었습니다."
alist = re.split('; | |, |\.|\n', cstr )
print(alist)

# 백슬래쉬를 사용할때는 re를 사용하면 안된다.
astr  = r"Beaut\iful, is; bet\ter*th\an\nugly"
alist = astr.split('\\')
print(alist)