
import re   #regular expression 정규

astr  = 'Beautiful, is; bet\ter*than\nugly'
alist = re.split('; | |,|\*|\n', astr )
print(alist)

s = "one two 3.4 5,6 seven.eight nine,ten"
blist = re.split('\s|(?<!\d)[,.](?!\d)', s)
print(blist)

cstr="무궁화 꽃이 피었습니다.정말 아름답게 피었습니까?이것들아!말을 해라고."
alist = re.split('; | |, |\.|\n', cstr )
print(alist)


astr  = r"Beaut\iful, is; bet\ter*th\an\nugly"
alist = astr.split('\\')
print(alist)


cstr="무궁화 꽃이 피었습니다.정말 아름답게 피었습니까?이것들아!말을 해라고."
alist = re.split('\.|\?|\!', cstr )
print(alist)