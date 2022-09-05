# AirBnB_clone

The goal of the project is to deploy on your server a simple copy of the AirBnB website which features HTML/CSS templating, database storage, API, front-end integration etc. This version is just the implementation of the backend console. This project manipulates a storage system which gives us an abstraction between an `object`  and how they are persisted and stored. This abstraction would enable us to change the type of storage easily without updating all the codebase. The `console` will be a tool to validate this storage engine.


### Console
* create your data model
* manage (create, update, destroy, etc) objects via a console / command interpreter
* store and persist objects to a file (JSON file)

#### List of commands this console currently supports:
* `EOF` - exits console 
* `quit` - exits console
* `<emptyline>` - overwrites default emptyline method and does nothing
* `create` - Creates a new instance of`BaseModel`, saves it (to the JSON file) and prints the id
* `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file). 
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representation of all instances based or not on the class name. 
* `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). 


### Models directory 
#### contains all the classes used in this project
`base_model.py`: takes care of the initialization, serialization,deserialization of future instances(objects). Also serves as the base class other classes inherit from.


### Tests Directory
#### Contains all the unittest thats validates our classes and storage engine 

`file_storage.py` Abstracted storage of the project 

### Roadmap
* put in place a parent class (BaseModel) that takes care of the initialization, serialization and deserialization of future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine

### Installation
* Clone the repository `git clone https://github.com/LikemDzokoto/AirBnB_clone.git`
* Access the clone repo `cd AirBnB_clone`
* Run the console `./console.py`
