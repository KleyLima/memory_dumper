# -*- coding: utf-8 -*-

from utils.clear import clear
from utils.enter_data import Input


class ReservedArea:
    # Class Attributes
    BYTES_SECTOR = '[11:13]'
    SECTOR_CLUSTER = '[13]'
    SECTORS_RESERVED_AREA = '[14:16]'
    QTD_FAT = '[16]'
    QTD_DIRECTORY_ENTRY = '[17:19]'
    SECTORS_BY_FAT = '[22:24]'

    # List of parameters used to set values
    PARAMETERS = ['bytes_sector', 'sector_cluster', 'sectors_reserved_area', 'qtd_fat', 'qtd_directory_entry',
                  'sectors_by_fat']

    def __init__(self, double_check=False):
        self.dump = self.take_dump(double_check)
        self.bytes_sector = self.sector_cluster = self.sectors_reserved_area = self.qtd_fat = 0
        self.qtd_directory_entry = self.sectors_by_fat = 0
        self.bytes_sector_hex = self.sector_cluster_hex = self.sectors_reserved_area_hex = self.qtd_fat_hex = 0
        self.qtd_directory_entry_hex = self.sectors_by_fat_hex = 0

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
        clear()

        # Input
        stream = Input.enter_data(rows=2)

        # Double check trigger
        if double_check:
            check = Input.enter_data(rows=2, confirmation=True)
            if check != stream:
                clear()
                input("The data dont match, type all again, please.")
                self.take_dump(double_check=True)
        clear()
        return stream

    def get_parameters(self):
        """
        Call a function to assign values to the attributes listed in ATTRIBUTES's list
        :return: None
        """
        Input.set_parameters(self)

    def set_parameters(self):
        """
        Call a function to calculate value using hex values
        :return: None
        """
        Input.set_hex_values(self)

    def __repr__(self):
        return f"""Bytes per sector: {self.bytes_sector_hex}  \nSectors per cluster: {self.sector_cluster_hex}
                    Sectors of Reserved Area: {self.sectors_reserved_area_hex} \nQuantity of FAT's: {self.qtd_fat_hex}
                    \nQuantity of directory entries: {self.qtd_directory_entry_hex} 
                    \nSectors by FAT: {self.sectors_by_fat_hex}
                """


if __name__ == '__main__':
    na = ReservedArea(False)
    na.get_parameters()
    na.set_parameters()
    print(na.bytes_sector)
    print(na.BYTES_SECTOR)
    print(na.bytes_sector_hex)
    print(na.qtd_directory_entry_hex)
