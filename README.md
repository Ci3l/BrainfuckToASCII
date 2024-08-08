# Brainfuck to ASCII

This project provides a basic Brainfuck to ASCII and Integer conversion algorithm, available on the NumWorks Workshop [here](https://workshop.numworks.com/python/ciel/brainfuck2ascii).

## Description

The script translates Brainfuck code into ASCII characters and integers. It reads Brainfuck code, processes the commands, and outputs the result as ASCII characters and integers. This project aims to provide a straightforward implementation of Brainfuck interpretation, helping users understand how Brainfuck code can be converted to readable characters.

## Features

- **Brainfuck Interpretation:** Converts Brainfuck commands into corresponding ASCII characters.
- **Input Handling:** Supports inputs provided as space-separated integers for the Brainfuck `,` command.
- **Memory Management:** Utilizes an array to manage memory cells, with a pointer to navigate through them.

## Usage

To use the script, call the `BrainF` function with the Brainfuck code and optional input values:

```python
def BrainF(code, entrees = None):
    
```

### Parameters
* **'code'**: A string containing Brainfuck code.
* **'entrees'**: (Optional) A space-separated string of integers to be used with the Brainfuck , command.

### Example
```python
BrainF('++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.')
```
This example translates Brainfuck code to ASCII characters, outputting "Hello World!" followed by a newline.

### Demo
To see the project in action, you can access the Brainfuck to ASCII algorithm on the NumWorks Workshop [here](https://workshop.numworks.com/python/ciel/brainfuck2ascii).

### Related Projects
[TextToBrainfuckTranslator](https://github.com/Ci3l/TextToBrainfuckTranslator): A Python-based translator that converts arbitrary text input into optimized Brainfuck code. This project was created to validate my understanding of ASCII encoding and Brainfuck, and to refine my Python programming skills. The goal of this tool is to generate the most compact Brainfuck code possible for any given string.

### Participation
I welcome contributions and suggestions for improving the script. Feel free to submit a pull request, open an issue, or send your feedback to [email](emailto:poire.erwan2005@gmail.com).

### License
This project is licensed under the MIT License - see the LICENSE file for details.
