## Memory Dumper

A helper to travel in the RAM Memory of a MS-DOS.

Considering the scenario:
  - A MS-DOS in Virtual Machine
  - A Intel 8086 Architeture.
  - A FAT12 FILE SYSTEM

The Code help following the adresses and infos using de The DEBUG command inside MS-DOS.

#

## Preparation

Download or clone the repo. Move to your desired location.

To make imports work:
  - In a terminal go to location of the project and type `export PYTHONPATH=$(pwd)`

Now just run the entrypoint in the interactive mode with `python3 -i dumper.py` and follow the program instructions.

## Using

Start typing the info about the reserved area of the memory.

After that type info about the FAT region.

So the console will be free, use the `ram` variable to perform operations, like:
  - Get general info about the RAM itself with `ram` command
  - Add a file with `ram.new_file()` and follow the command prompt
  - List registred file/directories with `ram.files`
  - Calculate the command needed to reach some cluster with `ram.calc_offset_to_cluster()`

## Testing

Before using it for real learn how thing works with the test inputs from the `inputs/` directory.

#


The majority off the functions are documented, make some read for your own good. 
Any improvements make a PR, a fork and let's make it better.

Make a good use.
