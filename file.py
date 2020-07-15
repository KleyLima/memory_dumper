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

    def __init__(self):
        self.path = self.filename = self.file_extension = self.date = self.hour = self.file_size = self.atrib = 0
        self.used_clusters = self.is_directory = self.dump = self.init_cluster = 0
        self.filename_hex = self.file_extension_hex = self.date_hex = self.hour_hex = self.file_size_hex = 0
        self.atrib_hex = self.init_cluster_hex = Hex("0")
        self.exist_atribs = []
        self.hour_real = self.date_real = 0
        self.take_dump()
        self.get_parameters()
        self.set_parameters()
        self.get_string_values()
        self.read_attributes()
        self.calc_hour()

    def get_string_values(self):
        self.filename = Input.string_from_stream(self.filename)
        self.file_extension = Input.string_from_stream(self.file_extension)

    def read_attributes(self):
        """
        Read the stream of data and fetch the correct attribute types for the file
        :return: None
        """
        self.exist_atribs = Bin(self.atrib_hex).get_active_bits()

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


if __name__ == '__main__':
    na = File()
    print(na.filename, na.file_extension, na.atrib)  # , 'hour', 'date', 'init_cluster')
    print(na.hour_real)
