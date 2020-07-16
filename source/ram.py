# -*- coding: utf-8 -*-

from source.fat import Fat
from source.file import File
from source.reserved_area import ReservedArea, Hex


class RAM(ReservedArea):

    def __init__(self):
        super().__init__()
        self.fats_size = self.root_dir_size = Hex("0")
        self.root_dir_offset = self.files_subdir_offset = Hex("0")
        self.fat = None
        self.calc_offsets_sizes()
        self.enter_fat()
        self.files = []

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
        out_put = super().__repr__()
        out_put += f"\n------------------RAM MEMORY---------------------------------------------------" \
                   f"\nSum size of all FAT's {self.fats_size} \nRoot DIR Size: {self.root_dir_size}" \
                   f"\nComand to get in ROOT DIR: D {self.root_dir_offset.vl_hex} " \
                   f"\nComand to get in FILES AND SUBDIRS: D {self.files_subdir_offset.vl_hex}" \
                   f"\nComand to get in the start of FAT: D {self.reserved_area_size}" \
                   f"\nFiles tracked: {len(self.files)}" \
                   f"\nAcess file with ram.files[index of file]" \
                   f"\nTrack a new file with ram.new_file()" \
                   f"\n--------------------------------------------------------------------------"
        return out_put

    def enter_fat(self):
        input(f"Time to FAT's dump, use the command D {self.reserved_area_size.vl_hex} in MS-DOS.")
        self.fat = Fat()

    def new_file(self):
        print(f"Time to input the data of a file, go to ROOT DIR with: D {self.root_dir_offset.vl_hex}")
        print(f"Type a file that you dont have typed before, each file uses 20h bytes = 2 lines in debug screen.")
        self.files.append(File(fat_map=self.fat.dump))

    def calc_offset_to_cluster(self):
        cluster = input("Input the cluster that you want the offset to(hex): ")
        offset = Hex.calc_cluster_hex(reserved_area_size=self.reserved_area_size.vl_hex, fats_size=self.fats_size.vl_hex
                                      , root_dir_size=self.root_dir_size.vl_hex, cluster=cluster,
                                      cluster_size=self.bytes_sector_hex.vl_hex)
        print(f"Use the command: D {offset} to {cluster} cluster")
        print(f"For the lasts 32 chars of {cluster}-1 cluster use D [{offset} - 20h]")


if __name__ == '__main__':
    na = RAM()
    na.new_file()
    na.files[0].calc_used_clusters()
    print(na.files[0].used_clusters)
    na.calc_offset_to_cluster()
