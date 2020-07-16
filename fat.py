# -*- coding: utf-8 -*-

from reserved_area import ReservedArea, Input


class Fat(ReservedArea):
    def __init__(self):
        self.dump = []
        self.take_dump(rows=4)

    def __repr__(self):
        return "------------------------FAT DATA--------------------------------------------------" \
               f"\nMap of FAT: {self.dump}" \
               f"----------------------------------------------------------------------------------"

    @staticmethod
    def input_warnings():
        print("Go to the start in FAT memory. Consult FAT offset!")

    def extend_fat(self):
        print(f"You are about to expand FAT. In the moment : {self.dump}")
        rows = int(input("How many lines im debug are needed?"))
        self.dump.extend(Input.enter_data(rows=rows))


if __name__ == '__main__':
    na = Fat()
    print(na)
