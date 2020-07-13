# -*- coding: utf-8 -*-

class Hex:
    
    def __init__(self, vl_hex):
        self.vl_hex = vl_hex
        self.vl_dec = self.to_decimal()

    def to_decimal(self):
        return int(f"0x{self.vl_hex}", 16)


    def __mul__(self, other):
        if isinstance(other, Hex):
            return Hex(format(self.vl_dec * other.vl_dec, 'X'))


# cmd = "echo 'obase=16;ibase=16;1.8*3' | bc"
# out = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
# out.stdout.decode('utf-8')

na = Hex('a')
no = Hex('a')
print(na.vl_hex, na.vl_dec)
res = na * no
print(res.vl_dec, res.vl_hex)

