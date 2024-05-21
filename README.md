<div style="text-align: center;">
<h1 style="color: blue; font-size: 2em;"> 0x00. AirBnB clone - The console </h1>  
<img src="./images/hbnb.png" alt="Image description" title="Image Title" />
<br>
<br>
<h1 style="color: blue; font-size: 2em;">Tools Using</h1>
<img src="./images/using_tools.png" alt="Image description" title="Image Title" />
<br>
<br>  
  <h1 style="color: blue; font-size: 2em;">Data_daigram</h1>
  <img src="./images/Data_daigram.jpg" alt="Image description" title="Image Title" />

</div>

![N|Solid](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240310%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240310T135420Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7747110f46f470ed821b025fbae85eae4d15c10ed5ab49e9e60d8ef239109a34)

# 0x00. AirBnB clone - The console
___
In The AirBnB clone project we aims to develop a command-line application that mimics the functionality of the popular online rental marketplace, AirBnB. The project focuses on building a command interpreter in Python to manage various objects within the AirBnB system, such as users, states, cities, and places.

Key objectives of the project:
* Implementing a parent class (BaseModel) to handle object initialization, serialization, and deserialization.
* Creating classes for different AirBnB objects that inherit from BaseModel
* Developing a file storage engine for data persistence.
* Create of unit tests to validate the functionality of classes and the storage engine.

### Command Interpreter Overview
The command interpreter allows users to interact with the AirBnB system through a series of commands. It enables users to perform various operations on objects, including creation, retrieval, updating, and deletion.

> Starting the Command Interpreter
```sh
$ ./console.py
(hbnb)
```
> Using the Command Interpreter
```sh
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
```

#### Examples
Here are some examples of how users can interact with the command interpreter:

1. Creating a new user:
```sh
(hbnb) create BaseModel
47d4bb6e-7b6d-4505-a055-fabacdc101d1
```
2. Listing all available objects:
```sh

(hbnb) all BaseModel
["[BaseModel] (e08df09f-88b4-4092-94a6-e5c8097e4aad) {'id': 'e08df09f-88b4-4092-94a6-e5c8097e4aad', 'created_at': datetime.datetime(2024, 3, 10, 21, 41, 4, 139592), 'updated_at': datetime.datetime(2024, 3, 10, 21, 41, 4, 139610)}", "[BaseModel] (47d4bb6e-7b6d-4505-a055-fabacdc101d1) {'id': '47d4bb6e-7b6d-4505-a055-fabacdc101d1', 'created_at': datetime.datetime(2024, 3, 10, 21, 41, 56, 754352), 'updated_at': datetime.datetime(2024, 3, 10, 21, 41, 56, 754365)}"]
```

2. Retrieving an object by ID:
```sh
(hbnb) show BaseModel 47d4bb6e-7b6d-4505-a055-fabacdc101d1
[BaseModel] (47d4bb6e-7b6d-4505-a055-fabacdc101d1) {'id': '47d4bb6e-7b6d-4505-a055-fabacdc101d1', 'created_at': datetime.datetime(2024, 3, 10, 21, 41, 56, 754352), 'updated_at': datetime.datetime(2024, 3, 10, 21, 41, 56, 754365)}
```
3. Updating an object's attribute:
```sh
(hbnb) update BaseModel 47d4bb6e-7b6d-4505-a055-fabacdc101d1 name "Holberton"
(hbnb) show BaseModel 47d4bb6e-7b6d-4505-a055-fabacdc101d1
[BaseModel] (47d4bb6e-7b6d-4505-a055-fabacdc101d1) {'id': '47d4bb6e-7b6d-4505-a055-fabacdc101d1', 'created_at': datetime.datetime(2024, 3, 10, 21, 41, 56, 754352), 'updated_at': datetime.datetime(2024, 3, 10, 21, 43, 42, 209793), 'name': '"Holberton"'}
```
4. Deleting an object:
```sh
(hbnb) destroy BaseModel 47d4bb6e-7b6d-4505-a055-fabacdc101d1
(hbnb) show BaseModel 47d4bb6e-7b6d-4505-a055-fabacdc101d1
** no instance found **
```

