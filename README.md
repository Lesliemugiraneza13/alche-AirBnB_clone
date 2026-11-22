# AirBnB Clone - The Console

## Description

AirBnB clone is a multi-step project whose goal is to build a simplified copy of the AirBnB website. Over the course of the project it grows into a complete web application made of:

- a **command interpreter** to manipulate data without a visual interface (this repository, step one)
- a **website** (front-end) with static and dynamic pages
- a **storage engine** (JSON files first, then a database)
- an **API** that connects the front-end to the data

This first step builds the foundation: a data model, a file-based storage engine, and a console to manage objects. Everything built here is reused in the following steps.

## How it works

Objects (users, places, reviews, ...) are Python instances of classes that inherit from `BaseModel`. They are persisted with the following flow:

```
instance -> to_dict() -> dictionary -> JSON string -> file.json
file.json -> JSON string -> dictionary -> instance
```

The `FileStorage` engine handles this flow, so the rest of the code never needs to know how objects are stored. Every time the program starts, it reloads all previously saved objects from `file.json`.

## Project structure

| Path | Purpose |
| --- | --- |
| `console.py` | Entry point of the command interpreter |
| `models/base_model.py` | `BaseModel`, the parent class of all models |
| `models/user.py`, `state.py`, `city.py`, `amenity.py`, `place.py`, `review.py` | Classes inheriting from `BaseModel` |
| `models/engine/file_storage.py` | `FileStorage`, JSON serialization and deserialization |
| `tests/` | Unit tests, mirroring the project layout |
| `AUTHORS` | List of contributors |

## The command interpreter

### Requirements

- Ubuntu 20.04 LTS
- Python 3.8.5
- Code style: `pycodestyle` 2.7.*

### Starting the console

Interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) quit
$
```

Non-interactive mode:

```
$ echo "help" | ./console.py
```

### Available classes

`BaseModel`, `User`, `State`, `City`, `Amenity`, `Place`, `Review`

### Commands

| Command | Usage | Description |
| --- | --- | --- |
| `help` | `help [command]` | Lists commands, or shows help for one command |
| `quit` / `EOF` | `quit` | Exits the program (`EOF` is Ctrl+D) |
| `create` | `create <class name>` | Creates a new instance, saves it, and prints its id |
| `show` | `show <class name> <id>` | Prints the string representation of an instance |
| `destroy` | `destroy <class name> <id>` | Deletes an instance and saves the change |
| `all` | `all [class name]` | Prints all instances, optionally only those of one class |
| `update` | `update <class name> <id> <attribute name> "<attribute value>"` | Adds or updates one attribute of an instance and saves the change |

Notes on `update`:

- Only one attribute can be updated at a time; extra arguments are ignored.
- Values containing spaces must be wrapped in double quotes.
- `id`, `created_at` and `updated_at` cannot be updated.

### Error messages

| Message | Meaning |
| --- | --- |
| `** class name missing **` | No class name was given |
| `** class doesn't exist **` | The class name is not a known class |
| `** instance id missing **` | No id was given |
| `** no instance found **` | No instance exists for that class name and id |
| `** attribute name missing **` | `update` was called without an attribute name |
| `** value missing **` | `update` was called without a value |

### Examples

```
$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', ...}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) all MyModel
** class doesn't exist **
(hbnb) quit
$
```

## Testing

Run all unit tests:

```
python3 -m unittest discover tests
```

Run a single test file:

```
python3 -m unittest tests/test_models/test_base_model.py
```

The tests also pass in non-interactive mode:

```
echo "python3 -m unittest discover tests" | bash
```

## Authors

See the [AUTHORS](AUTHORS) file for the list of contributors.
