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
import re
import shlex


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
        EOF (Ctrl+D) signal to exit the program.
        """
        return True

    def emptyline(self):
        """
        Do nothing on empty input line.
        """
        pass

    def do_help(self, arg):
        """
        help manual
        """
        cmd.Cmd.do_help(self, arg)

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        """
        command_arg = shlex.split(arg)

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
        """
        command_arg = shlex.split(arg)
        try:
            if len(command_arg) == 0:
                print("** class name missing **")
            elif command_arg[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(command_arg) < 2:
                print("** instance id missing **")
            else:
                class_name = command_arg[0]
                instance_id = command_arg[1].strip('"')
                objs = storage.all()
                key = "{}.{}".format(class_name, instance_id)
                if key in objs:
                    print("[{}] ({}) {}".
                          format(class_name, instance_id, objs[key].__dict__))
                else:
                    print("** no instance found")
        except Exception:
            pass

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        command_arg = shlex.split(arg)
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
        """
        objs = storage.all()
        command_arg = shlex.split(arg)
        if len(command_arg) == 0:
            for key, value in objs.items():
                print(str(value))
        elif command_arg[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            for key, value in objs.items():
                if key.split('.')[0] == command_arg[0]:
                    print(str(value))

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute.
        """
        command_arg = shlex.split(arg)

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
                obj = objs[key]
                braces = re.search(r"\{(.*?)\}", arg)
                if braces:
                    str_data = braces.group(1)
                    # convert str_data into python object and back to dict
                    a_dict = eval("{" + str_data + "}")
                    # Convert the arguments in the dict into list
                    arg_names = list(a_dict.keys())
                    arg_values = list(a_dict.values())

                    atr_name1 = arg_names[0]
                    atr_value1 = arg_values[0]

                    atr_name2 = arg_names[1]
                    atr_value2 = arg_values[1]

                    setattr(obj, atr_name1, atr_value1)
                    setattr(obj, atr_name2, atr_value2)
                else:
                    atr_name = command_arg[2]
                    atr_value = command_arg[3]
                    try:
                        atr_value = eval(atr_value)
                    except Exception:
                        pass
                    setattr(obj, atr_name, atr_value)

                    obj.save()

    def do_count(self, arg):
        """
        Counts and retrieves the number of instances of a class
        """
        objs = storage.all()
        command_arg = shlex.split(arg)

        if arg:
            class_nam = command_arg[0]

        count = 0

        if command_arg:
            if class_nam in self.classes:
                for obj in objs.values():
                    if obj.__class__.__name__ == class_nam:
                        count += 1
                print(count)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")

    def default(self, arg):
        """
        Catches commands that are not explicitly defined.
        Commands handled are like <class name>.all(),
        <class name>.count(), <class name>.destroy(),
        <class name>.update()
        """
        arg_lst = arg.split('.')
        inc_cls_nam = arg_lst[0]  # incoming class name
        command_arg = arg_lst[1].split('(')  # Incoming arguments
        inc_cmd_meth = command_arg[0]  # incoming command method
        inc_ex_arg = command_arg[1].split(')')[0]  # incoming extra arguments

        # all_args = inc_ex_arg.split('.')

        meth_dict = {
                'all': self.do_all,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update,
                'count': self.do_count
                }

        if inc_cmd_meth in meth_dict.keys():
            if inc_cmd_meth != "update":
                # Method construct
                return meth_dict[inc_cmd_meth]("{} {}".format(inc_cls_nam,
                                                              inc_ex_arg))
            else:
                # object_id = all_args[0]
                # attr_name = all_args[1]
                # attr_value = all_args[2]
                obj_id, a_dict = split_braces(inc_ex_arg)

                try:
                    if isinstance(a_dict, str):
                        str_attr = a_dict
                        return meth_dict[inc_cmd_meth]("{} {} {}".format
                                                       (inc_cls_nam, obj_id,
                                                        str_attr))
                    elif isinstance(a_dict, dict):
                        dict_attr = a_dict
                        return meth_dict[inc_cmd_meth]("{} {} {}".format
                                                       (inc_cls_nam, obj_id,
                                                        dict_attr))
                except Exception:
                    print("** argument missing **")

        print("*** Unknown syntax: {}".format(arg))
        return False


def split_braces(inc_ex_arg):
    """
    Splits the braces for the update method
    """
    braces = re.search(r"\{(.*?)\}", inc_ex_arg)

    if braces:
        unique_id = shlex.split(inc_ex_arg[:braces.span()[0]])
        id = [i.strip(",") for i in unique_id][0]

        str_data = braces.group(1)
        try:
            a_dict = eval("{" + str_data + "}")
        except Exception:
            print("**  invalid dictionary format **")
            return
        return id, a_dict
    else:
        command_arg = inc_ex_arg.split(",")
        if command_arg:
            try:
                id = command_arg[0]
            except Exception:
                return "", ""
            try:
                atr_name = command_arg[1]
            except Exception:
                return id, ""
            try:
                atr_value = command_arg[2]
            except Exception:
                return id, atr_name
            return f"{id}", f"{atr_name} {atr_value}"


if __name__ == '__main__':
    HBNBCommand().cmdloop()
