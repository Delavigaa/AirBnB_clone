#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json

class HBNBCommand(cmd.Cmd):
	"""
	HBNBCommand is a command-line interface class that extends cmd.Cmd.
	It provides a set of commands for interacting with the HBNB application.
	"""

	prompt = '(hbnb) '
	classes = {
		"BaseModel": BaseModel,
		"User": User,
		"State": State,
		"City": City,
		"Amenity": Amenity,
		"Place": Place,
		"Review": Review
	}

	def do_quit(self):
		"""Quit command to exit the program"""
		return True

	def do_EOF(self):
		"""Exit the program"""
		return True

	def do_create(self, arg):
		"""Create a new instance of BaseModel"""
		if not arg:
			print("** class name missing **")
			return
		try:
			new_instance = self.classes[arg]()
			new_instance.save()
			print(new_instance.id)
		except KeyError:
			print("** class doesn't exist **")

	def do_show(self, arg):
		"""Print the string representation of an instance"""
		args = arg.split()
		if not args:
			print("** class name missing **")
			return
		try:
			class_name = args[0]
			instance_id = args[1]
			instance = storage.get(class_name, instance_id)
			if instance:
				print(instance)
			else:
				print("** no instance found **")
		except IndexError:
			if len(args) == 1:
				print("** instance id missing **")
			else:
				print("** class doesn't exist **")

	def default(self, line):
		"""Method called on an input line when the command prefix is not recognized."""
		if '.' in line:
			args = line.split('.')
			class_name = args[0]
			command = args[1]
			if command == 'all()':
				self.do_all(class_name)
			elif command == 'count()':
				self.do_count(class_name)
			elif 'show(' in command and ')' in command:
				id = command.split('(')[1].split(')')[0]
				self.do_show(f"{class_name} {id}")
			elif 'destroy(' in command and ')' in command:
				id = command.split('(')[1].split(')')[0]
				self.do_destroy(f"{class_name} {id}")
			elif 'update(' in command and ')' in command:
				params = command.split('(')[1].split(')')[0].split(', ')
				id = params[0]
				if '{' in params[1] and '}' in params[1]:
					attribute_dict = json.loads(params[1])
					self.do_update_with_dict(f"{class_name} {id}", attribute_dict)
				else:
					attribute_name = params[1]
					attribute_value = params[2]
					self.do_update(f"{class_name} {id} {attribute_name} {attribute_value}")
			else:
				print("*** Unknown syntax: {}".format(line))
		else:
			print("*** Unknown syntax: {}".format(line))

	def do_update_with_dict(self, arg, attribute_dict):
		"""Update an instance based on the class name and id with a dictionary."""
		args = arg.split()
		if not args:
			print("** class name missing **")
			return
		try:
			class_name = args[0]
			instance_id = args[1]
			instance = storage.get(class_name, instance_id)
			if instance:
				for key, value in attribute_dict.items():
					setattr(instance, key, value)
				instance.save()
			else:
				print("** no instance found **")
		except IndexError:
			if len(args) == 1:
				print("** instance id missing **")
			else:
				print("** class doesn't exist **")

	def do_count(self, arg):
		"""Counts the number of instances of a class."""
		instances = storage.all()
		count = sum(1 for obj in instances.values() if obj.__class__.__name__ == arg)
		print(count)

	def do_destroy(self, arg):
		"""Delete an instance based on the class name and id"""
		args = arg.split()
		if not args:
			print("** class name missing **")
			return
		try:
			class_name = args[0]
			instance_id = args[1]
			instance = storage.get(class_name, instance_id)
			if instance:
				storage.delete(instance)
				storage.save()
			else:
				print("** no instance found **")
		except IndexError:
			if len(args) == 1:
				print("** instance id missing **")
			else:
				print("** class doesn't exist **")

	def do_all(self, arg):
		"""Print all string representations of instances"""
		args = arg.split()
		if args and not args[0]:
			print("** class doesn't exist **")
			return
		instances = storage.all()
		if args:
			class_name = args[0]
			instances = {k: v for k, v in instances.items() if v.__class__.__name__ == class_name}
		print([str(v) for v in instances.values()])

	def do_update(self, arg):
		"""Update an instance based on the class name and id"""
		args = arg.split()
		if not args:
			print("** class name missing **")
			return
		try:
			class_name = args[0]
			instance_id = args[1]
			instance = storage.get(class_name, instance_id)
			if instance:
				if len(args) < 3:
					print("** attribute name missing **")
				elif len(args) < 4:
					print("** value missing **")
				else:
					attribute_name = args[2]
					attribute_value = args[3]
					setattr(instance, attribute_name, attribute_value)
					instance.save()
			else:
				print("** no instance found **")
		except IndexError:
			if len(args) == 1:
				print("** instance id missing **")
			else:
				print("** class doesn't exist **")

if __name__ == '__main__':
	HBNBCommand().cmdloop()
