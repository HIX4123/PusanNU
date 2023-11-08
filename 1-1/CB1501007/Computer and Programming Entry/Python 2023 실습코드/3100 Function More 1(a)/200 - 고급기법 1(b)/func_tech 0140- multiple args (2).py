# parameter의 갯수를 미리 정하지 않고


def good( **kargs ) :
    for key, values in kargs.items() :
        print(f' key={key}, value={values}')



good(summer=10)
good(tomato=10, banana="맛있다", msg="이건 뭐여?")