# python-filedump.
filedump compares the first few bytes of given files

While coding another project, I came accross a bug where my program couldn't load a certain jpg file, but was able to load other jpg files.
I wanted to compare the first few bytes of the jpg in question, with the other jpg files that would load, side by side. Hence, filedump was created.


Example input:
```
C:\Users\User\Python> python filedump.py image1.jpg image2.jpg
```

Example output:
```
image1.jpg        image2.jpg

0 11111111 FF     0 01010010 52 R
1 11011000 D8     1 01001001 49 I
2 11111111 FF     2 01000110 46 F
3 11100000 E0     3 01000110 46 F
4 00000000 00     4 10100100 A4
5 00010000 10     5 01011110 5E
6 01001010 4A J   6 00000000 00
7 01000110 46 F   7 00000000 00
8 01001001 49 I   8 01010111 57 W
9 01000110 46 F   9 01000101 45 E
A 00000000 00     A 01000010 42 B
B 00000001 01     B 01010000 50 P
C 00000001 01     C 01010110 56 V
D 00000001 01     D 01010000 50 P
E 00000000 00     E 00111000 38 8
F 01100000 60     F 00100000 20
```

Example input:
```
C:\Users\User\Python> python filedump.py -h
```

Example output:
```
filedump outputs the first <bytes> of a file(s).

                        Output format:
<hex addr>  <byte in binary>  <byte in hex>  <byte as char>

Use:
  filedump.py [options] file1 [file2, file3...]

Options:
 <any number>,   How many bytes to display, defaults to 16.

           -k,   Will keep the script alive by requiring the enter key to be pressed
                  before exiting. This is useful if it launches in another window.
```
