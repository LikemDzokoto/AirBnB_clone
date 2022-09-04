#!/usr/bin/python3
'''
Console that contains the Entry-point of the AirBnB_clone command interpreter
'''

import cmd


class HBNBCommand(cmd.Cmd):
    ''' The bash-like Console '''
    prompt = '(hbnb) '

    def do_EOF(self, command):
        '''End of file reached\n'''
        return True

    def do_quit(self, command):
        '''Quit command to exit the program\n'''
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
