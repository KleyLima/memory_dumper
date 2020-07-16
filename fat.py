# -*- coding: utf-8 -*-

from reserved_area import ReservedArea, Input


class Fat(ReservedArea):
    def __init__(self):
        self.fat_map = None
        self.dump = 0
        self.take_dump()

    def __repr__(self):
        return "------------------------FAT DATA--------------------------------------------------" \
               f"\nMap of FAT: {self.dump}" \
               f"----------------------------------------------------------------------------------"

    @staticmethod
    def input_warnings():
        print("Go to the start in FAT memory. Consult FAT offset!")

    def extend_fat(self):
        print(f"You are about to expand FAT. In the moment : {self.fat_map}")
        rows = int(input("How many lines im debug are needed?"))
        self.fat_map.extend(Input.enter_data(rows=rows))


if __name__ == '__main__':
    na = Fat()
    print(na)
