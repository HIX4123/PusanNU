
def f(x, y=None):
    if y is None: y = []
    y.append(x)
    return y

print("\n실험-01 ----------")
print(f(23))

# Check if a default parameter value being used
def saver(x=None):
     if x is None:         # no argument passed?
         x = []            # run code to make a new list
     x.append(100)         # changes new list object
     print(x)
print("\n실험-02 ----------")
saver([2])
saver()                   # doesn't grow here
saver()

# Give the parameters in the function default values
def hello_3(greeting='Hello', name='world'):
    print('%s, %s!' % (greeting, name))

print("\n실험-03 ----------")
hello_3()
hello_3('Greetings')
hello_3('Greetings', 'universe')
hello_3(name='Gumby')


def hello_4(name, greeting='Hello', punctuation='!'):
    print('%s, %s%s' % (greeting, name, punctuation))

print("\n실험-04 ----------")
hello_4('Mars')
hello_4('Mars', 'Hi')
hello_4('Mars', 'Hi', '...')
hello_4('Mars', punctuation='.')
hello_4('Mars', greeting='It is a greeting!')

