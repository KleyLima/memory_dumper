# -*- coding: utf-8 -*-

from utils.clear import clear


class Input:

    @staticmethod
    def enter_data(rows, confirmation=False):
        """
        Read the data stream from the input, aggregationg in a single list
        :param rows: Number of rows that will be read from input
        :param confirmation: Flag if this is a confirmation call of the method
        :return: List of strings
        """
        input("Type again for confirmation. PRESS ENTER") if confirmation else None
        clear()
        stream = []
        [stream.extend(input("Type the {} line: ".format(turn + 1)).split()) for turn in range(rows)]
        return stream
