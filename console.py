#!/usr/bin/python3
'''
Console that contains the Entry-point of the AirBnB_clone command interpreter
'''

import cmd
import models


class HBNBCommand(cmd.Cmd):
    ''' The bash-like Console '''
    prompt = '(hbnb) '

    def do_EOF(self, command):
        '''Quit command to exit the program\n'''
        return True

    def do_quit(self, command):
        '''Quit command to exit the program\n'''
        return True

    def emptyline(self):
        ''' empty line + ENTER excecutes nothing'''
        pass

    def do_create(self, class_name):
        '''creates a new instance, saves it to file & prints the id'''
        if class_name:
            if class_name == 'BaseModel':
                instance = models.BaseModel()
                instance.save()
                print(instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, commands):
        '''prints string representation of instance as class.id'''
        if commands:
            commands = commands.split()
            if commands[0] == 'BaseModel':
                if len(commands) > 1:
                    my_key = f"{commands[0]}.{commands[1]}"
                    instances_in_file = models.storage.all()
                    if my_key in instances_in_file:
                        print(instances_in_file[my_key])
                    else:
                        print("** no instance found **")
                else:
                    print('** instance id missing **')
            else:
                print("** class doesn't exist **")
        else:
            print('** class name missing **')

    def do_destroy(self, line):
        ''' deletes an instance based on c_name and id, save changes '''
        if line:
            line = line.split()
            if line[0] == 'BaseModel':
                if len(line) > 1:
                    my_key = f"{commands[0]}.{commands[1]}"
                    instances_in_file = models.storage.all()
                    if my_key in instances_in_file:
                        del instances_in_file[my_key]
                    else:
                        print("** no instance found **")
                else:
                    print('** instance id missing **')
            else:
                print("** class doesn't exist **")
        else:
            print('** class name missing **')



if __name__ == '__main__':
    HBNBCommand().cmdloop()
