
quote = 'Let it be, let it be, let it be'

result = quote.rfind('let it')  # 꺼꾸로
print("Substring 'let it':", result)

result = quote.rfind('small')
print("Substring 'small ':", result)

result = quote.rfind('be,')
if  (result != -1):  # 없는 경우
  print(("Highest index where 'be,' occurs:", result))
else:
  print ("Doesn't cont")



mstat="This is a sample file where a rabbit loves in a there"