#!/usr/bin/python3
"""Module for command interpreter enty point"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for HBNB
    """
    prompt = "(hbnb) "
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on empty input line.
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        Usage: create <class name>
        """
        command_arg = arg.split()

        try:
            if not arg:
                print("** class name missing **")
            elif arg not in self.classes:
                print("** class doesn't exist **")
            else:
                new_instance = eval(f"{command_arg[0]}()")
                storage.save()
                print(new_instance.id)
        except Exception:
            pass

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the
        class name and id.
        Usage: show <class name> <id>
        """
        command_arg = arg.split()
        try:
            if len(command_arg) == 0:
                print("** class name missing **")
            elif command_arg[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(command_arg) < 2:
                print("** instance id missing **")
            else:
                objs = storage.all()
                key = "{}.{}".format(command_arg[0], command_arg[1])
                if key in objs:
                    print(objs[key])
                else:
                    print("** no instance found")
        except Exception:
            pass

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Usage: destroy <class name> <id>
        """
        command_arg = arg.split()
        try:
            if len(command_arg) == 0:
                print("** class name missing **")
            elif command_arg[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(command_arg) < 2:
                print("** instance id missing **")
            else:
                objs = storage.all()
                key = "{}.{}".format(command_arg[0], command_arg[1])
                if key not in objs:
                    print("** no instance found **")
                else:
                    del objs[key]
                    storage.save()
        except Exception:
            pass

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Usage: all [<class name>]
        """
        command_arg = arg.split()

        objs = storage.all()
        obj_list = []

        if len(command_arg) == 0:
            for key, value in objs.items():
                obj_list.append("[{}] ({}) {}".format(value.__class__.__name__, value.id, value.__dict__))
        elif command_arg[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            for key, value in objs.items():
                if key.split('.')[0] == command_arg[0]:
                    obj_list.append("[{}] ({}) {}".format(value.__class__.__name__, value.id, value.__dict__))
                    print(obj_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        command_arg = arg.split()

        if len(command_arg) == 0:
            print("** class name missing **")
        elif command_arg[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(command_arg) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()
            key = "{}.{}".format(command_arg[0], command_arg[1])
            if key not in objs:
                print("** no instance found **")
            elif len(command_arg) < 3:
                print("** attribute name missing **")
            elif len(command_arg) < 4:
                print("** value missing **")
            else:
                objs = storage.all()[key]
                setattr(objs, command_arg[2], command_arg[3].strip('"'))
                objs.save()

    def do_count(self, class_name):
        """
        Counts and retrieves the number of instances of a class
        usage: <class name>.count()
        """
        if not class_name:
            print("** class name missing **")
        elif class_name not in self.classes:
            print("** class doesn't exist **")
        else:
            count = sum(1 for obj in storage.all().values()
                        if obj.__class__.__name__ == class_name)
            print(count)

    def default(self, line):
        """
        Catches commands that are not explicitly defined.
        Here, we handle commands like <class name>.all()
        and <class name>.count().
        """
        command_arg = line.split('.')

        if len(command_arg) == 2:
            class_name, method_call = command_arg[0], command_arg[1].strip()
            if class_name in self.classes:
                if method_call == "all()":
                    self.do_all(class_name)
                elif method_call == "count()":
                    self.do_count(class_name)
                else:
                    print("*** Unknown syntax: {}".format(line))
            else:
                print("** class doesn't exist **")
        else:
            print("*** Unknown syntax: {}".format(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
