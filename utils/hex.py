# -*- coding: utf-8 -*-

import subprocess


class Hex:

    def __init__(self, vl_hex):
        self.vl_hex = vl_hex.upper()
        self.vl_dec = self.to_decimal()

    @classmethod
    def create_a_int_hex(cls, float_hex):
        """
        Strip the decimal part of a number and create a Hex int
        :param float_hex: String representing a float Hex
        :return: Hex instance
        """
        new = float_hex.split('.')[0]
        return cls(vl_hex=new)

    def to_decimal(self):
        try:
            return int(f"0x{self.vl_hex}", 16)
        except ValueError as err:
            print(err)
            return None

    def __mul__(self, other):
        """
        Multiplication of two instance of Hex.
        :param other: Hex's class Instance
        :return: A Hex object
        """
        if isinstance(other, Hex):
            return Hex.create_a_int_hex(float_hex=self.calc_by_bc(other=other))

    def __repr__(self):
        return f"Hex: {self.vl_hex}h Dec: {self.vl_dec if self.vl_dec else 'Fail dec convert'}"

    def calc_by_bc(self, other):
        """
        Realize the given calc in hex in the GNU's bc (basic calculator)
        :param other: Instance of Hex's class
        :return: A string representing the result of the multiplication
        """
        cmd = f"echo 'obase=16;ibase=16;{self.vl_hex}*{other.vl_hex}' | bc"
        out = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
        return out.stdout.decode('utf-8')[:-1]



na = Hex('a.8')
print(na)
no = Hex('a')
print(na)
res = na * no
print(res)
# cmd = f"echo 'obase=16;ibase=16;3*1.8' | bc"
# out = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
# na = out.stdout.decode('utf-8')
# print(repr(na))