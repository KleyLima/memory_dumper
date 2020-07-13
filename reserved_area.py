# -*- coding: utf-8 -*-

from utils.clear import clear
from utils.enter_data import Input


class ReservedArea:
    BYTES_SECTOR = '[12:14]'
    SECTOR_CLUSTER = '[14]'
    SECTORS_RESERVED_AREA = '[15:17]'
    QTD_FAT = '[17]'
    QTD_DIRECTORY_ENTRY = '[18:20]'
    SECTOR_BY_FAT = '[23:25]'

    def __init__(self, double_check=False):
        self.dump = self.take_dump(double_check)

    def take_dump(self, double_check=False):
        """
        Use the data in memory to instrospect the attributes of file system.
        The correct data passing is user's responsabilty.
        :param double_check: For who want warrancy against mistyping with this flag on you have to type the data
        twice to check if are equal. This do not deny the fact that you can get wrong equal two times.
        """
        clear()
        # Instructions
        print("Run the DEBUG program in MS-DOS")
        print("Load the floppy data into the RAM memory")
        print("In MS-DOS: L 0 0 0 70")
        print("Dump the Reserved Area's memory region")
        print("In MS-DOS: D 0")
        input("Copy each line just like are in DOS's terminal except for '-' between byte 7 and 8.")

        # Input
        stream = Input.enter_data(rows=2)
        print(stream)

        # Double check trigger
        if double_check:
            check = Input.enter_data(rows=2, confirmation=True)
            if check != stream:
                clear()
                input("The data dont match, type all again, please.")
                self.take_dump(double_check=True)

        return stream


if __name__ == '__main__':
    na = ReservedArea(True)
    print(na.dump)
