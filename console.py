#!/usr/bin/env python3
""" this is a command line interepter for the airbnb clone"""

import cmd
import os
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from pprint import pprint


def cast(str):
    """catsts the input string to the its actual data type"""
    if str.isdigit():
        return int(str)
    else:
        try:
            res = float(str)
            return res
        except ValueError:
            return str


class HBNBCommand(cmd.Cmd):
    """Simple airbnb console."""
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "Place",
               "State", "City", "Amenity", "Review"]

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_clear(self, line):
        """clears the console"""
        os.system("clear")

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it and prints the id
        """
        if not line:
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            class_name = globals()[line]
            new = class_name()
            new.save()
            print(new.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            id = f"{args[0]}.{args[1]}"
            instance_obj = storage.all().get(id)
            if not instance_obj:
                print("** no instance found **")
            else:
                print(instance_obj)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            all_objs = storage.all()
            id = f"{args[0]}.{args[1]}"
            instance_dict = all_objs.get(id)
            if not instance_dict:
                print("** no instance found **")
            else:
                del all_objs[id]
                storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances"""
        instances = []
        all_objects = storage.all()
        if not line:
            for obj in all_objects.values():
                instances.append(obj.__str__())
        elif line and line not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            for obj in all_objects.values():
                if type(obj).__name__ == line:
                    instances.append(obj.__str__())
        print(instances)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        error = 0
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            error = 1
        elif len(args) == 1:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                error = 1
            else:
                print("** instance id missing **")
                error = 1
        else:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            all_objs = storage.all()
            id = f"{args[0]}.{args[1]}"
            instance = all_objs.get(id)
            if not instance:
                print("** no instance found **")
                error = 1
        if error:
            return
        if len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            attr_name = args[2]
            attr_value = args[3]
            setattr(instance, attr_name, cast(attr_value))
            instance.save()

    def default(self, line):
        """default method for the console"""
        syntax_error = f"*** Unknown syntax: {line}"
        args = line.split(".")
        if len(args) == 1:
            print(syntax_error)
        else:
            class_name = args[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            if args[1] == "count()":
                counter = 0
                all_objects = storage.all()
                for obj in all_objects.values():
                    if type(obj).__name__ == class_name:
                        counter += 1
                print(counter)
            elif args[1] == "all()":
                self.do_all(class_name)
            elif args[1][:5] == "show(" and args[1][-1] == ")":
                id = args[1][5:-1].strip("\"'")
                self.do_show(f"{class_name} {id}")
            elif args[1][:8] == "destroy(" and args[1][-1] == ")":
                id = args[1][8:-1].strip("\"'")
                self.do_destroy(f"{class_name} {id}")
            else:
                print(syntax_error)

    def emptyline(self):
        """if no command entered it displays a new prompt"""
        pass


if __name__ == "__main__":
    """this is the main"""
    HBNBCommand().cmdloop()
