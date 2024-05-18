![Console](images/airbnb.png)

# AirBnB Clone Project

This is a simplified clone of the AirBnB web application. The goal of this project is to understand the fundamental concepts of higher-level programming and web development. This project involves building a console for managing various models, including users, places, cities, and amenities, and allows for the storage and retrieval of these models.

## Table of Contents

- [Description](#description)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Commands](#commands)
- [Command Interpreter](#command-interpreter)
  - [How to Start It](#how-to-start-it)
  - [How to Use It](#how-to-use-it)
  - [Examples](#examples)
- [Models](#models)
- [Testing](#testing)
- [Authors](#authors)

## Description

This project is the first step towards building a full web application similar to AirBnB. It includes a console that can create, retrieve, update, and delete instances of various models, as well as save these instances to and load them from a JSON file.

## Getting Started

### Prerequisites

- Python 3.x
- `cmd` module (part of the Python standard library)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/AirBnB_clone.git
cd AirBnB_clone
```
## Usage
=======
2. Usage

To start the console, run:
```
python console.py
```

## Commands

Here are the available commands in the console:
```
quit or EOF: Exit the console
help <command>: Display help information about a command
create <ClassName>: Create a new instance of ClassName
show <ClassName> <id>: Show the instance of ClassName with the specified id
destroy <ClassName> <id>: Delete the instance of ClassName with the specified id
all [ClassName]: Show all instances of ClassName, or all instances if no class is specified
update <ClassName> <id> <attribute name> <attribute value>: Update the instance of ClassName with the specified id, adding or updating the specified attribute
<ClassName>.all(): Retrieve all instances of ClassName
<ClassName>.count(): Retrieve the number of instances of ClassName
<ClassName>.show(<id>): Retrieve an instance based on its ID
<ClassName>.destroy(<id>): Destroy an instance based on its ID
<ClassName>.update(<id>, <attribute name>, <attribute value>): Update an instance based on its ID with a specified attribute and value
<ClassName>.update(<id>, <dictionary representation>): Update an instance based on its ID with a dictionary of attributes
```

# Command Interpreter

### How to Start It
To start the command interpreter, run:
```
python console.py
```
### How to Use It
You can use the command interpreter to manage your models by typing commands at the prompt. Each command allows you to perform a specific action on the models.
For example, you can create new instances, retrieve existing ones, update them, and delete them.

### Examples
Here are some examples of how to use the command interpreter:
### Create a new instance of a model:
```
(hbnb) create User - This will create a new User instance and print its id.
```
### Show an instance of a model:
```
(hbnb) show User (id) - This will print the string representation of the User instance with the specified id.
```
### Destroy an instance of a model:
```
(hbnb) destroy User (id) - This will delete the User instance with the specified id.
```
### Update an instance of a model:
```
(hbnb) update User (id) - This will update the email attribute of the User instance with the specified id.
```
### Retrieve all instances of a model:
```
(hbnb) all User - This will print a list of all User instances.
```
### Retrieve the number of instances of a model:
```
(hbnb) User.count() - This will print the number of User instances.
```

## Models

The project includes several models, each represented by a Python class. These models inherit from the BaseModel class and include:
```
User: Represents a user with attributes like email, password, first name, and last name.
State: Represents a state with a name attribute.
City: Represents a city with a state ID and name attribute.
Amenity: Represents an amenity with a name attribute.
Place: Represents a place with attributes like city ID, user ID, name, description, number of rooms, number of bathrooms, maximum guests, price by night, latitude, longitude, and a list of amenity IDs.
Review: Represents a review with attributes like place ID, user ID, and text.
```

## Testing

Unit tests are provided for the console and models. To run the tests, use the following command:
```
python -m unittest discover tests
```

## Authors
```
Musyoki Dominic
Precious Oromoni
```
Feel free to contribute to this project by submitting pull requests. If you encounter any issues, please report them on the project's GitHub page.
