
from timeit import Timer



def listTest():
    list_data=[3,2,1,4,7,9,5,8,6,10,11,12,14,13,15,19,20,18,16,17,\
               875,345,123,32,45,98,5432,4353,65,99]
    list_data.index(14)   # return 12. position in list


def tupleTest():
    tuple_data=(3,2,1,4,7,9,5,8,6,10,11,12,14,13,15,19,20,18,16,17,\
                875,345,123,32,45,98,5432,4353,65,99)
    tuple_data.index(14)    # return 12. position in list


t_listTest = Timer(listTest)  # returns the number of seconds it took to execute the code
print( f"list  Tester: {t_listTest.timeit():10.7}")


t_tupleTest = Timer(tupleTest)  # returns the number of seconds it took to execute the code
print( f"tuple Tester: {t_tupleTest.timeit():10.7}")