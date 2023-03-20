# Simple 6502 Emulator
# (CC-BY) R Mark Adams, Ph.D. 2023
from sys import argv, exit
from util6502 import *

def start_emulation(cpu, mem, hexfile = '', loadloc = '0200h', registers=[0,0,0,0,0,0,0]):
    """Initiate the emulator, optionally loading the memory from the designated hexfile

    Arguments:
    cpu -- instance of Cpu (cpu) class to emulate (REQUIRED)
    mem -- instance of Mem (memory) class to emulate (REQUIRED)

    Keyword Arguments:
    hexfile -- the (optional) input hexfile to load into memory before start
    loadloc -- starting point for the hexfile data load
    registers -- start state for the 6502 registers prior to run

    :return:
    Register and Stack Dump -- {'registers':{'A':<A>,'X':<X>,'Y':<Y>,'S':<S>,'PC':<PC>,'P':<P>},
        'flags':{'N':'N','V':'V','B':'B','D':'D','I':'I','Z':'Z','C':'C'}}
    """
    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    """Startpoint for the emulator

    Usage: pyemu_6502 [-i <input hexfile>] [-h]
        Where the <hexfile> is in standard *.hex format, bytes in ascii hexadecimal format.
        Example:
            23 FF CA 34 9F 0A 01 FF
            
    Output: Stack Dump in the following format:
            A=<A acumulator>
            X=<X index register>
            Y=<Y index register>
            S=<S stack pointer>
            PC=<PCH PCL program counter (high and low bytes)>
            P=<P processor status register - all flags as a single byte>
            <P flags bit-wise>
            N=<N sign (negative) flag>
            V=<V overflow flag>
            -
            B=<B break flag>
            D=<D decimal flag>
            I=<I interrupt flag>
            Z=<Z zero flag>
            C=<C carry flag>
    """
    myargs = getopts(argv)
    print(argv)
    if '-h' in myargs:
        # I know there is a way to print the docstring here - this is just a placeholder
        print()
        exit()
    if '-f' in myargs:
        print(f"Running emulator with hexfile {myargs['-f']}")
        my_hex = myargs['-f']
    start_emulation()

