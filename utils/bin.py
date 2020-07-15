# -*- coding: utf -8

from utils.hex import Hex


class Bin:

    def __init__(self, value_hex: Hex):
        self.vl_bin = 0
        self.get_bin(value_hex.vl_dec)

    @staticmethod
    def bin_to_dec(value_bin):
        return int(f"0b{value_bin}", 2)

    def get_bin(self, value_dec):
        self.vl_bin = format(value_dec, 'b') if value_dec else None

    def get_active_bits(self):
        return [pos for pos, data in enumerate(self.vl_bin[::-1]) if int(data)]


if __name__ == '__main__':
    na = Hex('70B1')
    no = Bin(na)
    print(no.get_active_bits())
