# -*- coding: utf -8 -*-

from reserved_area import ReservedArea
from utils.enter_data import Input


class File(ReservedArea):
    FILENAME = '[:8]'
    FILE_EXTENSION = '[8:11]'
    ATRIB = '[11]'
    HOUR = '[22:24]'
    DATE = '[24:26]'
    INIT_CLUSTER = '[26:28]'
    FILE_SIZE = '[28:32]'

    PARAMETERS = ['filename', 'file_extension', 'atrib', 'hour', 'date', 'init_cluster']

    def __init__(self):
        self.path = self.filename = self.file_extension = self.date = self.hour = self.file_size = self.atrib = 0
        self.used_clusters = self.is_directory = self.dump = 0
        self.take_dump()
        self.get_parameters()
        self.set_parameters()
        self.get_string_values()

    def get_string_values(self):
        self.filename = Input.string_from_stream(self.filename)
        self.file_extension = Input.string_from_stream(self.file_extension)


if __name__ == '__main__':
    na = File()
    print(na.filename, na.file_extension, na.atrib)  # , 'hour', 'date', 'init_cluster')
