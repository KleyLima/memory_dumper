# -*- coding: utf -8 -*-

from reserved_area import ReservedArea, Hex
from utils.bin import Bin
from utils.enter_data import Input


class File(ReservedArea):
    FILENAME = '[:8]'
    FILE_EXTENSION = '[8:11]'
    ATRIB = '[11]'
    HOUR = '[22:24]'
    DATE = '[24:26]'
    INIT_CLUSTER = '[26:28]'
    FILE_SIZE = '[28:32]'

    PARAMETERS = ['filename', 'file_extension', 'atrib', 'hour', 'date', 'init_cluster', 'file_size']
    ATTRIBS = ["Somente Leitura", "Arquivo Oculto", "Arquivo de Sistema", "Nome do Volume", "Entrada de sub-diretório",
               "Arquivo modificado"]

    def __init__(self, parent_folder="\\"):
        self.filename = ""
        self.file_extension = self.date = self.hour = self.file_size = self.atrib = 0
        self.used_clusters = self.is_directory = self.dump = self.init_cluster = 0
        self.filename_hex = self.file_extension_hex = self.file_size_hex = 0
        self.path = parent_folder
        self.atrib_hex = self.init_cluster_hex = self.date_hex = self.hour_hex = Hex("0")
        self.exist_atribs = []
        self.nested_files = []
        self.hour_real = self.date_real = 0
        self.take_dump()
        self.get_parameters()
        self.set_parameters()
        self.get_string_values()
        self.read_attributes()
        self.calc_hour()
        self.calc_date()

    def get_string_values(self):
        self.filename = Input.string_from_stream(self.filename)
        self.file_extension = Input.string_from_stream(self.file_extension)

    def read_attributes(self):
        """
        Read the stream of data and fetch the correct attribute types for the file
        :return: None
        """
        self.exist_atribs = Bin(self.atrib_hex).get_active_bits()
        self.is_directory = True if self.ATTRIBS.index("Entrada de sub-diretório") in self.exist_atribs else False

    def calc_hour(self):
        """
        Get hour, min and sec of the last modification of the file using hex and bin numbers.
        :return: None
        """
        bin_repr = Bin(self.hour_hex)
        str_bin = bin_repr.vl_bin.zfill(16)
        sec = Bin.bin_to_dec(str_bin[11:]) * 2
        minut = Bin.bin_to_dec(str_bin[5:11])
        hour = Bin.bin_to_dec(str_bin[:5])

        self.hour_real = f"{hour}:{minut}:{sec}"

    def calc_date(self):
        """
        Get year, month and year of the last modification of the file using hex and bin numbers.
        :return: None
        """
        bin_repr = Bin(self.date_hex)
        str_bin = bin_repr.vl_bin.zfill(16)
        year = Bin.bin_to_dec(str_bin[:7]) + 1980
        month = Bin.bin_to_dec(str_bin[7:11])
        day = Bin.bin_to_dec(str_bin[11:])

        self.date_real = f"{day}/{month}/{year}"

    def __repr__(self):
        return f"\n---------------------------{'FILE' if not self.is_directory else 'DIR'}---------------------------" \
               f"\nPath:{self.path}" \
               f"\nFilename: {self.filename} \nExtension: {self.file_extension}" \
               f"\nAttributes: {[att for index, att in enumerate(self.ATTRIBS) if index in self.exist_atribs]}" \
               f"\nDate: {self.date_real} \nHour: {self.hour_real} \nFile Size: {self.file_size_hex}" \
               f"\nNested Files: {[file.__repr__() for file in self.nested_files] if self.is_directory else None}" \
               f"\n--------------------------------------------------------------------------------------------------"

    # TODO: Nested files for subdir, or handle it in the RAM class ? if isdir [file for file in nested_files] and so on

    def append_file_to_dir(self):
        if self.is_directory:
            self.nested_files.append(File(parent_folder=self.path + self.filename))
        else:
            print("The current file is not a SUB-DIR")

    # TODO: Make a input_warning method for custom message for each class using the take_dump


if __name__ == '__main__':
    na = File()
    print(na)
