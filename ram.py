# -*- coding: utf-8 -*-

from reserved_area import ReservedArea, Hex


class RAM(ReservedArea):

    def __init__(self):
        super().__init__()
        self.fats_size = 0
        self.root_dir_size = 0
        self.root_dir_offset = 0
        self.files_subdir_offset = 0
        self.calc_offsets_sizes()

    def calc_offsets_sizes(self):
        """
        Calc the offset needed in ram to dump certain regions of memory.
        The 20h size of directories entry is a constant in this architecture.
        Note: fats are calculated together.
        :return: None
        """
        self.fats_size = self.qtd_fat_hex * self.sectors_by_fat_hex * self.bytes_sector_hex
        self.root_dir_size = self.qtd_directory_entry_hex * Hex("20")
        self.root_dir_offset = self.reserved_area_size + self.fats_size
        self.files_subdir_offset = self.root_dir_offset + self.root_dir_size

    def __repr__(self):
        out_put = f"\n------------------RAM MEMORY---------------------------------------------------" \
                  f"\nSum size of all FAT's {self.fats_size} \nRoot DIR Size: {self.root_dir_size}" \
                  f"\nComand to get in ROOT DIR: D {self.root_dir_offset.vl_hex} " \
                  f"\nComand to get in FILES AND SUBDIRS: D {self.files_subdir_offset.vl_hex}" \
                  f"\n--------------------------------------------------------------------------"
        out_put += super().__repr__()
        return out_put


if __name__ == '__main__':
    na = RAM()
    print(na)
