

# Matrixocity Compiler

Matrixocity is a **Python-dependent DSL (Domain-Specific Language)** inspired by Brainfuck but designed for **2D memory manipulation**.  
It introduces **two tapes** (`x_tape` and `y_tape`) for horizontal and vertical pointer operations, plus **logging, math, conditionals, and I/O**.  

This compiler translates `.mxt` source files into Python (`.py`) and automatically compiles them to `.pyc`.

---

## 📜 Features

- **Two-dimensional tapes**:
  - `x_tape` → Horizontal memory with `x_pointer`
  - `y_tape` → Vertical memory with `y_pointer`
- **Arithmetic & storage commands** (`+`, `-`, square, variables)
- **Input/output** with ASCII and integer modes
- **Logging** → Execution values automatically recorded in `vals.log`
- **Conditionals (`!if;`)** for simple jumps
- **Comment support** → Ignore code sections with `(` and `)`
- **Strict syntax validation** → Missing `;` triggers a `SyntaxError`

---

## 📂 Project Structure

```

Matrixocity/
├── compiler.py     # The compiler
├── example.mxt     # Example Matrixocity source file
├── vals.log        # Execution log (generated at runtime)
└── README.md

````

---

## 🚀 Usage

### 1. Write a `.mxt` file
Example (`hello.mxt`):
```mxt
@INIT;

!add;
!add;
!printa;   ( prints "B" )
!printr;   ( logs ASCII value of "B" )

@END
````

### 2. Compile it

```bash
python3 compiler.py hello.mxt
```

### 3. Run the compiled Python

```bash
python3 hello.py
```

Output will appear on screen, and all values are also stored in `vals.log`.

---

## 📖 Language Reference

### 🔹 Structure

Every Matrixocity program must start and end with:

```
@INIT;
... code ...
@END
```

---

### 🔹 Commands – `x_tape`

| Command    | Description                                           |
| ---------- | ----------------------------------------------------- |
| `!add;`    | Increment current `x_tape` cell by 1                  |
| `!minus;`  | Decrement current `x_tape` cell by 1                  |
| `!>;`      | Move pointer right                                    |
| `!<;`      | Move pointer left                                     |
| `!var;`    | Store current cell into variable `a`                  |
| `!var;`    | Restore variable `a` into current cell                |
| `!square;` | Square the value in current cell                      |
| `!printa;` | Print **ASCII character** at current cell, also logs  |
| `!printr;` | Print **integer value** at current cell, also logs    |
| `!inputl;` | Add integer input to current cell, also logs          |
| `+;`       | Add two numbers to current cell (experimental parser) |
| `!log;`    | Log current cell value to `vals.log` without printing |

---

### 🔹 Commands – `y_tape`

| Command    | Description                                           |
| ---------- | ----------------------------------------------------- |
| `!ADD;`    | Increment current `y_tape` cell by 1                  |
| `!MINUS;`  | Decrement current `y_tape` cell by 1                  |
| `!^;`      | Move pointer up                                       |
| `!yd;`     | Move pointer down                                     |
| `!SQUARE;` | Square the value in current cell                      |
| `!PRINTA;` | Print ASCII character of current cell, also logs      |
| `!PRINTR;` | Print integer value of current cell, also logs        |
| `!INPUTL;` | Add integer input to current cell, also logs          |
| `+y;`      | Add two numbers to current cell (experimental parser) |
| `!LOG;`    | Log current `y_tape` value to `vals.log`              |

---

### 🔹 Conditionals

| Command | Description                                                                  |
| ------- | ---------------------------------------------------------------------------- |
| `!if;`  | If `x_tape[x_pointer] != 0`, jump forward to the given offset (experimental) |

⚠️ The current `!if;` implementation is **experimental** and may not work reliably.
A future version will support structured control flow (`!if ... !endif`).

---

### 🔹 Comments

* Start: `(`
* End: `)`
* Everything between is ignored.

Example:

```mxt
( this is a comment )
!add;
```

---

## 📝 Logging

* All executed values are written to `vals.log` automatically.
* Example log after running:

  ```
  66
  B
  ```

---

## 📊 Example Program

```mxt
@INIT;

!add;
!add;
!add;
!printa;   ( prints "C" )
!printr;   ( prints 67 )

@END
```

Output:

```
C
67
```

Log (`vals.log`):

```
67C
67
```

---

## ⚠️ Limitations

* `!if;` and arithmetic shortcuts (`+;`, `+y;`) depend on fragile string parsing.
* Comments must be **line-based** (`(` and `)` on their own lines).
* Logs remain open until program exit (data flush happens at end).
* No sandboxing → **do not compile untrusted `.mxt` files**.

---

## 🧾 License

This project is free to use, modify, and share.

---

```
