import sys
import re


def is_gpr_operand(operand: str):
    return is_xzr(operand) or (operand.startswith("X") and operand[1:].isnumeric())


def is_xzr(operand: str):
    return operand == "XZR"


def is_sp(operand: str):
    return operand == "SP"


def verify(line: str):
    if not line:
        return True, ""
    # ignore labels
    if line.endswith(":"):
        return True, ""
    # ignore comment lines
    if line.startswith("/") or line.startswith("*"):
        return True, ""
    # ignore assembler directives
    if line.startswith("."):
        return True, ""

    # now we need to parse the actual instruction
    # chop off any comment if necessary
    line = line.split("//")[0].strip()

    opcode = line.split(" ")[0]

    # the opcodes for which there are no variants we have to check
    if opcode in [
        "LDUR",
        "STUR",
        "MOVK",
        "MOVZ",
        "MVN",
        "B",
        "BL",
        "RET",
        "NOP",
        "HLT",
        "ADRP",
    ]:
        return True, ""

    # b.cc
    # can probably do better with a regex capture group
    if opcode.startswith("B."):
        return True, ""

    # bcc
    if (
        opcode.startswith("B")
        and len(opcode) == 3
        and opcode[1:]
        in [
            "EQ",
            "NE",
            "CS",
            "HS",
            "CC",
            "LO",
            "MI",
            "PL",
            "VS",
            "VC",
            "HI",
            "LS",
            "GE",
            "LT",
            "GT",
            "LE",
            "AL",
        ]
    ):
        return True, ""

    # CMP, CMN, and TST
    if opcode in ["CMP", "CMN", "TST"]:
        # should be shifted register version.
        # of the form CMP <Xn>, <Xm>
        # Cannot use the shift!
        tokens = re.split(",\\s*|\\s+", line)
        if len(tokens) > 3:
            return (
                False,
                "using the shift on second operand or using the extended register version",
            )
        else:
            return True, ""

    # ALU_RR opcodes
    if opcode in ["ADDS", "SUBS", "ORR", "EOR", "ANDS"]:
        # Should be the shifted register version.
        # Of the form ADDS <Xd>, <Xn>, <Xm>
        # Cannot use the shift!
        tokens = re.split(",\\s*|\\s+", line)
        if len(tokens) > 4:
            return (
                False,
                "using the shift on second operand or using the extended register version",
            )
        elif not is_gpr_operand(tokens[3]):
            return False, "using an immediate for second operand"
        else:
            return True, ""

    # ALU_RI opcodes
    if opcode in ["ADD", "SUB", "LSL", "LSR", "ASR"]:
        # should be the immediate version
        # Of the form ADD <Xd|SP>, <Xn|SP>, #<imm>
        tokens = re.split(",\\s*|\\s+", line)
        if len(tokens) > 4:
            return (
                False,
                "using the shift on second operand or using the extended register version",
            )
        elif is_gpr_operand(tokens[3]) or is_sp(tokens[3]):
            return False, "using a register as second operand"
        else:
            return True, ""
    return False, "disallowed opcode"


if len(sys.argv) != 2:
    print('Usage: "python3 verify.py FILENAME"')
    exit(0)
fails = 0
with open(sys.argv[1], "r") as infile:
    for i, line in enumerate(infile, 1):
        (valid, reason) = verify(line.strip().upper())
        if not valid:
            fails += 1
            valid_instructions = False
            print(
                f"Line {i} failed verification. Reason: {reason}. \n\tLine contents: '{line.strip()}'"
            )

exit(fails)
