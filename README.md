# Memory Dumper

A helper to travel in the RAM Memory of a MS-DOS.

Considering the scenario:
  - A MS-DOS in Virtual Machine
  - A Intel 8086 Architeture.
  - A FAT12 FILE SYSTEM

The Code help following the adresses and infos using de The DEBUG command inside MS-DOS.

## How to use

Download or clone the repo. Move to your desired location.

To make imports work:
  - In a terminal go to location of the project and type `export PYTHONPATH=$(pwd)`

Now just run the entrypoint in the interactive mode with `python3 -i dumper.py` and follow the program instructions.

After the basic information you are free to manipulate the object "ram" to add files, review info, etc.

Make a good use.
