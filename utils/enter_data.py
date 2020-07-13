# -*- coding: utf-8 -*-

from utils.clear import clear
from utils.hex import Hex
from functools import reduce


class Input:

    @staticmethod
    def enter_data(rows, confirmation=False):
        """
        Read the data stream from the input, aggregating in a single list
        :param rows: Number of rows that will be read from input
        :param confirmation: Flag if this is a confirmation call of the method
        :return: List of strings
        """
        input("Type again for confirmation. PRESS ENTER") if confirmation else None
        clear()
        stream = []
        [stream.extend(input("Type the {} line: ".format(turn + 1)).split()) for turn in range(rows)]
        return stream

    @staticmethod
    def set_parameters(obj):
        """
        A few things are happening here. Every class that call this function should have a "PARAMETERS" class attribute
        that store the names of the parameters that are assigned by specif position of bytes in RAM memory.
        For each name in PARAMETERS mighty exist a class attribute with the same name with the region of the memory
        that points for the info needed.
        :param obj: Obj that will assing the values
        :return: None, its all about attribution
        """
        [setattr(obj, name_param, eval('{}{}'.format(obj.dump, getattr(obj, name_param.upper()))))
         for name_param in obj.PARAMETERS]

    @staticmethod
    def concat_stream(stream):
        """
        Takes the data that is in a list of string an group in one single string.
        The value saved in memory its REVERSED for the human readable concept, so its re-reversed now.
        NOTE: Alsos reverse things that are not save reversed (rare cases), e.g filename, fat type.
        :return: A String
        """
        stream.reverse() if isinstance(stream, list) else None
        return reduce(lambda k, l: k + l, stream)

    @staticmethod
    def set_hex_values(obj):
        [setattr(obj, f"{name_param}_hex", Hex(Input.concat_stream(getattr(obj, name_param))))
         for name_param in obj.PARAMETERS]
