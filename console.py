#!/usr/bin/python3
"""Entry point of the AirBnB clone command interpreter."""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

CLASSES = {"BaseModel": BaseModel, "User": User, "State": State,
           "City": City, "Amenity": Amenity, "Place": Place,
           "Review": Review}


def cast(value, current):
    """Cast the string value to the type of current, or guess its type."""
    if isinstance(current, bool) or current is None:
        pass
    elif isinstance(current, (int, float, str)):
        try:
            return type(current)(value)
        except ValueError:
            return value
    for kind in (int, float):
        try:
            return kind(value)
        except ValueError:
            continue
    return value


class HBNBCommand(cmd.Cmd):
    """Command interpreter used to manage the AirBnB objects."""

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF (Ctrl+D) exits the program
        """
        print()
        return True

    def _parse(self, arg, need_id=True):
        """Validate the arguments and return (args, instance) or None.

        Prints the matching error message when an argument is invalid.
        """
        try:
            args = shlex.split(arg)
        except ValueError:
            args = arg.split()
        if not args:
            print("** class name missing **")
            return None
        if args[0] not in CLASSES:
            print("** class doesn't exist **")
            return None
        if not need_id:
            return args, None
        if len(args) < 2:
            print("** instance id missing **")
            return None
        key = "{}.{}".format(args[0], args[1])
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
            return None
        return args, obj

    def do_create(self, arg):
        """Create a new instance, save it and print its id
        Usage: create <class name>
        """
        parsed = self._parse(arg, need_id=False)
        if parsed:
            obj = CLASSES[parsed[0][0]]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Print the string representation of an instance
        Usage: show <class name> <id>
        """
        parsed = self._parse(arg)
        if parsed:
            print(parsed[1])

    def do_destroy(self, arg):
        """Delete an instance and save the change
        Usage: destroy <class name> <id>
        """
        parsed = self._parse(arg)
        if parsed:
            args = parsed[0]
            del storage.all()["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """Print all instances, optionally only those of one class
        Usage: all [class name]
        """
        parsed = self._parse(arg, need_id=False) if arg.strip() else ([], 0)
        if parsed:
            name = parsed[0][0] if parsed[0] else None
            print([str(obj) for key, obj in storage.all().items()
                   if name is None or key.split(".")[0] == name])

    def do_update(self, arg):
        """Update an attribute of an instance and save the change
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        parsed = self._parse(arg)
        if not parsed:
            return
        args, obj = parsed
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        name = args[2]
        setattr(obj, name, cast(args[3], getattr(obj, name, None)))
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
