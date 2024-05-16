#!/usr/bin/python3
import cmd
import models
import models.engine
import models.engine.file_storage
class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    
    def do_quit(self, arg):
            '''Quit command to exit the program'''
            return True

    
    def do_EOF(self, arg):
            '''Exit the program 
            and print a newline 
            '''
            print('')  
            return True

    def emptyline(self):
            """Do nothing on empty line"""
            pass
    

    def do_create(self, arg):
        '''Create a new instance of the specified class'''
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.engine.file_storage.FileStorage.ALL_CLASS:
            print("** class doesn't exist **")
            return
        try:
            new_instance = models.engine.file_storage.FileStorage.ALL_CLASS[class_name]()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print("** {}".format(e))


    def do_show(self, arg):
        """Show information of a specific instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.engine.file_storage.FileStorage.ALL_CLASS:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])

    def do_destroy(self, arg):
        """Delete a specific instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.engine.file_storage.FileStorage.ALL_CLASS:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        del models.storage.all()[key]
        models.storage.save()

    def do_update(self, arg):
        """Update attributes of a specific instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.engine.file_storage.FileStorage.ALL_CLASS:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + "." + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = models.storage.all()[key]
        setattr(obj, args[2], args[3])
        models.storage.save()

    def do_all(self, arg):
        """Show all instances of a specified class"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.engine.file_storage.FileStorage.ALL_CLASS:
            print("** class doesn't exist **")
            return
        instances = [str(obj) for obj in models.storage.all().values() if type(obj).__name__ == class_name]
        print(instances)      

if __name__ == "__main__":
    HBNBCommand().cmdloop()
