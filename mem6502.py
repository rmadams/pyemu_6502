# Simple 6502 Emulator
# (CC-BY) R Mark Adams, Ph.D. 2023

# Memory classfile

import numpy as np

# hexfile sample data:
sample_hex = 'test_hexfile.hex'

class Mem:
    """Class which defines the 6502 memory

    """
    def __init__(self, size=4096, hexfile='', start_address=0):
        """Populate the initial state of the Memory

        Arguments:
            size -- size of memory in bytes (default 4096)
            hexfile -- initial memory load as a hexfile (default '' - None)
            start_address -- where to start loading the data from hexfile

        Usage:
        >>> my_mem = Mem()
        >>> my_mem.read_byte(0x0200)
        0
        """
        self.size = 4096
        self.hexfile = hexfile
        self.start_address = start_address
        self.data = [np.uint8(0x0) for item in range(self.size)]
        if hexfile != '':
            self.read_hexfile(self.hexfile,self.start_address)

    def read_byte(self, address):
        """Return the data at location <address>

        Parameters:
            address -- location in memory to read from

        Usage:
        >>> my_mem = Mem()
        >>> my_mem.write_byte(0x0200,0xA0)
        0
        >>> my_mem.read_byte(0x0200)
        160
        """
        if address <= self.size:
            return self.data[address]
        else:
            # Treat -1 as an error state
            return -1

    def write_byte(self,address,data):
        """Write a byte <data> to location <address> in the memory

        Parameters:
            address -- location in memory to read from
            data -- byte to write into memory

        Note:
            In order to ensure that what is written to memory is a single byte, <data> is mod 256

        Usage:
        >>> my_mem = Mem()
        >>> my_mem.write_byte(0x0200,0xA0)
        0
        >>> my_mem.read_byte(0x0200)
        160
        """
        if address <= self.size:
            self.data[address] = data % 256
            return 0
        else:
            # Treat -1 as an error state
            return -1

    def read_hexfile(self,hexfile,start_address=-1):
        """Read the data from <hexfile> into memory starting at the (optionally) designated <start_address>"""
        if start_address != -1:
            self.start_address = start_address
        with open(hexfile) as hexin:
            hexdat = [word for word in hexin.read().split()]
        for count in range(len(hexdat)):
            # Probably should replace this with the write_byte() method
            self.data[start_address+count] = int('0x'+ hexdat[count],16)

if __name__ == '__main__':
    """If the memory is working, you should be able to store and recall data, including loading data from a file
    
    Uaage:
    >>> my_mem = Mem(4096,'test_hexfile.hex',0x0200)
    >>> my_mem.read_byte(0x0200)
    169
    """
    my_mem = Mem(4096,'test_hexfile.hex',0x0200)
    print(my_mem.read_byte(0x0200))