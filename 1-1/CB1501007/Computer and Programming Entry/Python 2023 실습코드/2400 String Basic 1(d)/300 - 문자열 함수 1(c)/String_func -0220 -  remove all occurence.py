

word= "1,234,567,456,900"


w1 = word.replace(",","")
print(w1)
print(word)  #string은 immutable

unicode_line ="부산갈매기@#너는! 너는!! 정녕$"
translation_table = dict.fromkeys(map(ord, '!@#$'), None)
after = unicode_line.translate(translation_table)

print(f"after=", after)