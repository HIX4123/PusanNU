
container= list("착하게-살자!")

it = iter(container)
while True:
     try:
         e = next(it)
         print("> ", e)
     except StopIteration:
         break