# Simple 6502 Emulator
# (CC-BY) R Mark Adams, Ph.D. 2023

#CPU classfile

from mem6502 import Mem
import numpy as np
import inst6502

START = np.uint8(0x0200)  #default Program Counter start

class Cpu:
    """Class which defines the 6502 cpu

a = np.uint8(0b1100)
y = ~x
    """
    def __init__(self, mem, A=0, X=0, Y=0, S=0, PC=0, P=0):
        """Populate the initial state of the CPU"""
        self.A = np.uint8(0b0)  # Accumulator
        self.X = np.uint8(0b0)  # Index x register
        self.Y = np.uint8(0b0)  # Index Y register
        self.S = np.uint8(0b0)  # Stack register
        self.PC = START  # Program counter (composed of high- and low bytes in little-endian order as stored in PCH, PCL)
        self.P = np.uint8(0b0)  # Processor status register
        self.mem = mem
        self.done = False # The processor "run flag"

    def run(self):
        """The central CPU event loop"""
        while not self.done:
            # Pull the next instruction from memory pointed to by the Program Counter (PC)
            my_inst = self.mem.read_byte(self.PC)
            # Execute the selected instruction
            print(f"Executing: {inst6502.instructions[my_inst]}")
            inst6502.instructions[my_inst][3](cpu,mem)


