from utils import extract_code_blocks, translate_code, replace_code_blocks

def test_extract_code_blocks():
    sample_markdown = """
# Sample Markdown

Here's some code:
```python
print("Hello, World!")
```
And some more code:
```python
print("Hello, Again!")
```
"""
    extracted_blocks = extract_code_blocks(sample_markdown)
    print(extracted_blocks)
    assert len(extracted_blocks) == 2
    assert extracted_blocks[0] == '```python\nprint("Hello, World!")\n```'
    assert extracted_blocks[1] == '```python\nprint("Hello, Again!")\n```'

def test_translate_code():
    sample_code = 'print("Hello, World!")'
    translated = translate_code(sample_code, 'python', 'javascript')
    assert translated == """Translate the following python code to javascript:

print("Hello, World!")"""

def test_replace_code_blocks():
    sample_markdown = """
# Sample Markdown

Here's some code:
```python
print("Hello, World!")
```
"""
    translated_markdown = """
# Sample Markdown

Here's some code:
```js
console.log("Hello, World!");
```
"""
    replaced_content = replace_code_blocks(sample_markdown, ['```python\nprint("Hello, World!")\n```\n'], ['```js\nconsole.log("Hello, World!");\n```\n'])
    print(replaced_content)
    assert replaced_content == translated_markdown

"""
```cpp
255, 0377, 0xff             // Integers (decimal, octal, hex)
2147483647L, 0x7fffffffl    // Long (32-bit) integers
123.0, 1.23e2               // double (real) numbers
'a', '\\141', '\\x61'         // Character (literal, octal, hex)
'\\n', '\\\\', '\\'', '\\"'      // Newline, backslash, single quote, double quote
"string\\n"                  // Array of characters ending with newline and \\0
"hello" "world"             // Concatenated strings
true, false                 // bool constants 1 and 0
nullptr                     // Pointer type with the address of 0
```
"""

"""csharp
255, 0377, 0xff             // Integers (decimal, octal (not supported in C#), hex)
int.MaxValue, 0x7fffffff    // Int32 (32-bit) integers
123.0, 1.23e2               // double (real) numbers
'a', '\141', '\x61'         // Character (literal, octal, hex)
'\n', '\\', '\'', '\"'      // Newline, backslash, single quote, double quote
"string\n"                  // String ending with newline
"hello" + "world"           // Concatenated strings
true, false                 // bool constants true and false
null                        // Null reference for reference types in C#
"""