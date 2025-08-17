import random as rn
import time as ts
import sys


start = ts.time()

ya = 0
y_tape = [0]
xa = 0
x_tape = [0]
tape = [y_tape, x_tape]
x_pointer = 0
y_pointer = 0
code = ""
comment_mode = False
compiled_code = ""
nm = sys.argv[1].replace(".mxt", "")

with open(sys.argv[1], "r") as f:
    code = f.read()



if code.startswith("@INIT;") != True:
    raise SyntaxError("Code initilizer '@INIT;' not located at SoF or missing newline_identation at end.")
elif code.endswith("@END") != True:
    raise SyntaxError("Code closer '@END' not located at EoF.")
else:
    compiled_code += "import py_compile as pyc \ny_tape = [0] * 3000 \nx_tape = [0] * 3000 \ntape = [y_tape, x_tape] \nx_pointer = 0 \ny_pointer = 0 \nr = open('vals.log', 'w') \n"

    
## Matrixocity Compiler

for line in code.splitlines():
    code = code.strip()
    line = line.strip()
    if line == "@INIT;":
        if comment_mode:
            continue
        else:
            continue
    if line == "(":
        if comment_mode:
            continue
        else:
            comment_mode = True
    if line == ")":
        comment_mode = False
    elif line == "@END":
        if comment_mode:
            continue
        else:
            compiled_code += f"pyc.compile('{nm}.py', cfile='{nm}.pyc') \nquit()"
            continue
    elif line == "@var;":
        if comment_mode:
            continue
        else:
            compiled_code += f"a = tape[0][x_pointer] \n"
    elif line == "!var;":
        if comment_mode:
            continue
        else:
            compiled_code += f"tape[0][x_pointer] = a \n"
    elif line == "!add;":
        if comment_mode:
            continue
        else:
            compiled_code += "tape[0][x_pointer] += 1 \n"
    elif line == "!minus;":
        if comment_mode:
            continue
        else:
            compiled_code += "tape[0][x_pointer] -= 1 \n"
    elif line == "!>;":
        if comment_mode:
            continue
        else:
            compiled_code += "x_pointer += 1 \n"
    elif line == "!square;":
        if comment_mode:
            continue
        else:
            compiled_code += "tape[0][x_pointer] = tape[0][x_pointer] * tape[0][x_pointer] \n"
    elif line == "!SQUARE;":
        if comment_mode:
            continue
        else:
            compiled_code += "tape[1][y_pointer] = tape[1][y_pointer] * tape[1][y_pointer] \n"
    elif line == "!<;":
        if comment_mode:
            continue
        else:
            compiled_code += "x_pointer -= 1 \n"
    elif line == "!printa;":
        if comment_mode:
            continue
        else:
            compiled_code += "print(chr(tape[0][x_pointer]), end='') \nr.write(str(tape[0][x_pointer])) \n"
    elif line == "!printr;":
        if comment_mode:
            continue
        else:
            compiled_code += "print(tape[0][x_pointer]) \nr.write(str(tape[0][x_pointer])) \n"
    elif line == "!inputl;":
        if comment_mode:
            continue
        else:
            compiled_code += "tape[0][x_pointer] += int(input(f'Cell {x_pointer} >> ')) \nr.write(str(tape[0][x_pointer])) \n"
    elif line == "!if;":
        if comment_mode:
            continue
        else:
            compiled_code += f"""
code = '''{code.strip()}'''
line = '''{line.strip()}'''
if tape[0][x_pointer] != 0:
    x_pointer = int(code[code.strip().index(line) + 5])
            
            
"""
    elif line == "+;":
        if comment_mode:
            continue
        else:
            compiled_code += f"""
code = '''{code.strip()}'''
line = '''{line.strip()}'''
a = int(code[code.strip().index(line) - 2])
b = int(code[code.strip().index(line) + 3])
tape[0][x_pointer] += a + b

""" 
            

    elif line == "!ADD;":
        if comment_mode:
            continue
        else:
            compiled_code += "tape[1][y_pointer] += 1 \n"
    elif line == "!MINUS;":
        if comment_mode:
            continue
        else:
            compiled_code += "tape[1][y_pointer] -= 1 \n"
    elif line == "!^;":
        if comment_mode:
            continue
        else:
            compiled_code += "y_pointer += 1 \n"
    elif line == "!yd;":
        if comment_mode:
            continue
        else:
            compiled_code += "y_pointer -= 1 \n"
    elif line == "!PRINTA;":
        if comment_mode:
            continue
        else:
            compiled_code += "print(chr(tape[1][y_pointer]), end='') \n"
            compiled_code += "r.write(str(chr(tape[1][y_pointer])))\n"
    elif line == "!PRINTR;":
        if comment_mode:
            continue
        else:
            compiled_code += "print(tape[1][y_pointer]) \n"
            compiled_code += "r.write(str(tape[1][y_pointer]))\n"
    elif line == "!INPUTL;":
        if comment_mode:
            continue
        else:
            compiled_code += "tape[1][y_pointer] += int(input(f'Cell Y {y_pointer} >> ')) \n"
            compiled_code += "r.write(str(tape[1][y_pointer]))\n"
    elif line == "!LOG;":
        if comment_mode:
            continue
        else:
            compiled_code += "r.write(str(tape[1][y_pointer]))\n"
    elif line == "!log;":
        if comment_mode:
            continue
        else:
            compiled_code += "r.write(str(tape[0][x_pointer]))\n"
    elif line == ";":
        if comment_mode:
            continue
        else:
            continue
    elif line == "+y;":
        if comment_mode:
            continue
        else:
            compiled_code += f"""
code = '''{code.strip()}'''
line = '''{line.strip()}'''
a = int(code[code.strip().index(line) - 2])
b = int(code[code.strip().index(line) + 3])
tape[1][y_pointer] += a + b

"""         
    elif line.strip().endswith(";") != True:
        if line == "@END":
            continue
        elif ")" in line:
            continue
        elif line.isdigit():
            continue
        else:
            raise SyntaxError(f"{line} missing semi-colon")


with open(f"{nm}.py", "w") as f:
    end = ts.time()
    elapsed_time = (end - start) * 1000
    print(f"compiled in: {elapsed_time:.2f} ms")
    f.write(compiled_code)
