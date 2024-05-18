# AirBnB Clone Project

This is a simplified clone of the AirBnB web application. The goal of this project is to understand the fundamental concepts of higher-level programming and web development. This project involves building a console for managing various models, including users, places, cities, and amenities, and allows for the storage and retrieval of these models.

## Table of Contents

- [Description](#description)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Commands](#commands)
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

Musyoki Dominic
Precious Oromoni

Feel free to contribute to this project by submitting pull requests. If you encounter any issues, please report them on the project's GitHub page.
