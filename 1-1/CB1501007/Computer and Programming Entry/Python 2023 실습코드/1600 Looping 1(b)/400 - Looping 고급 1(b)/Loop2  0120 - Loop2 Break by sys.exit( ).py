import sys

def foo():
    print('foo')

actions = {'1': foo, '2': sys.exit}

def read_choice(choices, prompt):
    c = input("Type 1(foo) or 2(sys.exit) :")
    while c not in choices:
        print(" Error: 1과 2만 허용됩니다")
        c = input(prompt)
    return c

while True: # get user input
    x = read_choice(actions, 'Input 1 for foo( ) 또는  2 for exit( )')
    actions[x]() # act on it
