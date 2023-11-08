

import sys, cmd

class MyCmd(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "--> "
        self.list = []
    def do_add(self, x):                # add number
        if x and (x not in self.list):
            self.list.append(x)
    def help_add(self):         # add
        print('help for add')
    def do_show(self, x):       # show
        print(self.list)
    def help_show(self):                # show
        print('help for show')
    def do_EOF(self, x):                # EOF (Ctrl-Z  Ctrl-D)
        sys.exit()
    def help_EOF(self):         # EOF ???꾩?留?
        print('quit the program')

if __name__ == '__main__':
    c = MyCmd()
    c.cmdloop()
