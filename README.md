# Bulk-Import
Tools for automatically importing classes and modules in bulk.
Allowing you to add/change/remove features without needing to update the imports elsewhere.

## Application
Suppose you had a command parser. For the time being it only parses a hand full of commands, but you plan on adding more later.
For every command you wish to add, you must import it where it is needed/used.
If you have a lot of commands to add, or you import them in a lot of places, this can lead to a huge hastle every time you want to add a command.
By using bulk_import, you can have all of your command classes inherit from a Command base class,  store them all in a 'commands' folder, 
and then tell your python program to import all classes of type Command from the folder 'commands'.

The file structure would look something like this:
* project
	* command.py - this would contain the base class Command
	* commands - all command classes would be stored in here
		* command_a.py - these would inherit the base class Command
		* command_b.py
		* command_c.py
	
With this file structure, you can now clearly see where all your command classes are and what commands your program currently implements
And with this tool, you can import these commands with relative ease, even add/remove commands without changing any of the modules that import them.


## Usage
```python
from bulk_import import import_subclasses		# import_subclasses imports all classes of type base class from a particular directory
class BaseClass: pass 					# all subclasses would extend this class
subclasses = import_subclasses(				#
	directory = "directory.path.to.modules",	# required: the directory where all subclasses can be accessed
	base_class = BaseClass,				# required: the base class which all subclasses will be checked against.
	deepest_level = 3				# optional: default = 0, how many levels past the given directory the function is allowed to look
)							# 	This is useful if your subclasses are located in their own folder, not directly under the directory

```

## Installing
type "pip install bulkimporttools"

## Developement
Github repository is located here: https://github.com/Mikael-MStinson/Bulk-Import

Pypi project is located here: https://pypi.org/project/bulkimporttools/
