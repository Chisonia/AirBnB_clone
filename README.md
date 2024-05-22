Description
An AirBnB clone involves building a system that can manage users, listings, bookings, and reviews. The console component is a command-line interface (CLI) application that allows users to interact with the system by typing commands. This console is crucial for managing and testing the backend before integrating with a web interface. This console is crucial for managing and testing the backend before integrating with a web interface.

Command-line interpreter designed to simplify and streamline the interaction with our custom-built application. The interpreter allows users to execute a wide range of commands to manipulate and retrieve data, automate tasks, and customize their workflow.

How to Start It
To start the command interpreter, follow these steps:

Clone the Repository:
git clone https://github.com/your-username/AirBnB_clone.git
cd AirBnB_clone

Install Dependencies:
Ensure you have Python installed. Then, install any required dependencies:
pip install -r requirements.txt

Run the Interpreter:
Start the command interpreter by running
./console.py


How to Use It
The command interpreter is an interactive shell that allows you to interact with the application’s data models. You can create, retrieve, update, and delete objects using various commands.

Basic Commands
help: Displays a list of available commands or detailed information about a specific command.
help
help <command>
quit: Exits the command interpreter.

quit
EOF: Exits the command interpreter (End Of File).

EOF
create: Creates a new instance of a specified class.

create <class_name>
show: Shows the details of an instance based on the class name and ID.

show <class_name> <id>
destroy: Deletes an instance based on the class name and id

destroy <class_name> <id>
all: Shows all instances of a class, or all instances of all classes if no class name is provided.

all
all <class_name>

update: Updates an instance based on the class name and ID by adding or updating an attribute.

update <class_name> <id> <attribute_name> <attribute_value>


Examples
Some examples of how to use the command interpreter:

Creating a New User:

(hbnb) create User
d94f3f01-8f6c-41b2-924f-3a1b2e4d4086

Showing a User:
(hbnb) show User d94f3f01-8f6c-41b2-924f-3a1b2e4d4086
[User] (e54f3f01-9e6c-91j2-924f-3a1b2e4d4086) {'id': 'e54f3f01-9e6c-91j2-924f-3a1b2e4d4086', 'created_at': datetime.datetime(2024, 5, 22, 12, 0, 0), 'updated_at': datetime.datetime(2024, 5, 22, 12, 0, 0)}

Updating a User:

(hbnb) update User e54f3f01-9e6c-91j2-924f-3a1b2e4d4086 name "John Doe"

Destroying a User:

(hbnb) destroy User e54f3f01-9e6c-91j2-924f-3a1b2e4d4086

Listing All Users:
(hbnb) all User
["[User] (e54f3f01-9e6c-91j2-924f-3a1b2e4d4086) {'e54f3f01-9e6c-91j2-924f-3a1b2e4d4086', 'created_at': datetime.datetime(2024, 5, 22, 12, 0, 0), 'updated_at': datetime.datetime(2024, 5, 22, 12, 0, 0), 'name': 'John Doe'}"]
