# Simple 6502 Emulator
# (CC-BY) R Mark Adams, Ph.D. 2023
import inst6502
# 6502 Instruction set

from util6502 import *

#     05 69 04 8D
#     00 03 00


# instruction set as a dictionary lookup.
# Format:
# { <opcode>:[<opcode>, <mode>, <# bytes>, <function>], ...}
instructions = {
    0xA9: ['LDA', 'Immediate', 2, inst6502.lda_imm],
    0x69: ['ADC', 'Immediate', 2, inst6502.adc_imm],
    0x8D: ['STA', 'Absolute', 2, inst6502.sta_abs],
    0x0D: ['BRK', 'None', 1, inst6502.brk],
}

def set_A_NZ(cpu):
    """Set the N (negative result) and Z (zero result) flags based on A (accumulator)

    :param cpu: CPU instance
    :return: None
    """
    # Set N-flag and Z-flag if appropriate
    set_bit(cpu.P, 1, not (cpu.A))  # Z-flag
    set_bit(cpu.P, 7, testBit(cpu.A, 7))  # N-flag
    # More verbose version ---v
    # # Check for negative result, and change N flag to reflect it
    # if testBit(cpu.A, 7):
    #     set_bit(cpu.P, 7)
    # # Check for zero result, and change N flag to reflect it
    # if cpu.A == 0:
    #     set_bit(cpu.P, 1)


def lda_imm(cpu,mem):
    """Load Accumulator with Memory, Immediate. The accumulator is loaded with new data.

    :param cpu: instance of the CPU
    :param mem: instance of the memory
    :return: 0 for success, -1 for failure
    """
    # Fetch the next two bytes
    # Synthesize the appropriate (little-endian) memory address
    # Recall the memory contents at that location and place it in the accumulator (A)
    cpu.A = mem.read_byte(mem(cpu.PC+1) + 256*(mem(cpu.PC+2)))
    # Check and set the N and Z flags for A:
    set_A_NZ(cpu)
    cpu.PC = cpu.PC + 3
    return 0


def adc_imm(cpu,mem):
    """Add with carry - Immediate- setting the V, Z, nd N flags

    :param cpu: instance of the CPU
    :param mem: instance of the memory
    :return: 0 for success, -1 for failure

    Note:
    Technically, the overflow indicator, a special bit reserved for this
    purpose, and called a "flag," will be set when there is a carry from
    bit 6 into bit 7 and no external carry, or else when there is no carry
    from bit 6 into bit 7 but there is an external carry.

    in C:
    static void adc(uint8_t arg) {
        unsigned const sum = a + arg + carry;
        carry = sum > 0xFF;
        // The overflow flag is set when the sign of the addends is the same and
        // differs from the sign of the sum
        overflow = ~(a ^ arg) & (a ^ sum) & 0x80;
        zn = a /* (uint8_t) */ = sum;
    }
    """
    # Fetch the next two bytes
    # Synthesize the appropriate (little-endian) memory address
    # Recall the memory contents at that location and place it in the accumulator (A)

    my_add = mem.read_byte(mem(cpu.PC+1) + 256*(mem(cpu.PC+2)))
    my_sum = cpu.A + my_add + testBit(cpu.P,0)
    if my_sum > 0xFF:
        # Set the carry bit
        set_bit(cpu.P, 0, 1)
    # Mod A to manage an overflow
    my_sum = my_sum % 256
    # I am pretty sure that I don't have the overflow managed right
    if testBit(cpu.A,7) == testBit(my_add,7):
        if testBit(cpu.A,7) != testBit(my_sum,7):
            set_bit(cpu.P,6)
    cpu.A = my_sum
    set_A_NZ(cpu)
    cpu.PC = cpu.PC + 3
    return 0


def sta_abs(cpu, mem):
    """Store A in Memory, Absolute mode

    :param mem: Instance of memory class
    :param cpu: Instance of cpu class:
    :return:  None
    """
    mem.write_byte(mem.read_byte(mem(cpu.PC+1) + 256*(mem(cpu.PC+2))),cpu.A)
    cpu.PC = cpu.PC + 3
    return None


def brk(cpu,mem):
    """Nominally "Simulate Interrupt ReQuest (IRQ)" but as per this implentation, halt the emulator

    :param cpu: Instance of cpu class
    :return: None
    """
    cpu.done = True
    return None