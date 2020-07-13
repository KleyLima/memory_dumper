# -*- coding: utf-8 -*-

class ReservedArea:
    
    def __init__(cls, double_check=False):
        self.dump = self.take_dump(double_check)

    def take_dump(double_check=False)
    """
    Use the data in memory to instrospect the attributes of file system.
    The correct data passing is user's responsabilty.
    :param double_check: For who want warrancy against mistyping with this flag on you have to type the data
    twice to check if are equal. This do not deny the fact that you can get wrong equal two times.
    """
    # Instructions
    print("Run the DEBUG program in MS-DOS")
    print("Load the floppy data into the RAM memory")
    print("In MS-DOS: L 0 0 0 70")
    print("Dump the Reserved Area's memory region")
    print("In MS-DOS: D 0")
    print("Copy each line just like are in DOS's terminal except for '-' between byte 7 and 8.")
    
    # Input
    first_row = [data for data in input("Type the first 16 bytes. (WITH SPACE BETWEEN EACH ONE)").split()]
    second_row = [data for data in input("Type the second line. ").split()]
    third_row = [data for data in input("Type the third line. ").split()]
    fourth_row = [data for data in input("Type fourth line. ").split()]
    
    # Aggregation
    first_row.exted(second_row)
    first_row.extend(third_row)
    first_row.extend(fourth_row)

    # Double check trigger
    if double_check:
        check = self.take_dump()

    return first_row

