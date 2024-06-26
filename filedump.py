import os
import sys


###
### filedump was created to quickly compare the first few bytes of one PNG with another PNG 
### to aid in the debugging of another program. I thought it was useful...
###

def printhelp():
    print("\nfiledump outputs the first <bytes> of a file(s).")
    print("\n                        Output format:")
    print("<hex addr>  <byte in binary>  <byte in hex>  <byte as char>")
    print("\nUse:")
    print("  filedump.py [options] file1 [file2, file3...]")
    print("\nOptions:")
    print(" <any number>,   How many bytes to display, defaults to 16.")
    print("\n           -k,   Will keep the script alive by requiring the enter key to be pressed")
    print("                 before exiting. This is useful if it launches in another window.")
    print("\n           -h,   Display this help message")
    if keepalive : input("Press enter to exit")
    exit()

paths = []        # Used to store valid paths
displaynames = [] # Used to store file names without their path, for output
invalidargs = []  # Used to store invalid arguments, currently not being used
output = []       # Used to store each row of formatted output
columnwidths = [] # Holds the maximum width of each column
padding = 2       # Adds space between each column
numbytes = 16     # Number of bytes to display
outputhwidth = 0  # Will hold the default output width. hexchars effects this.
hexchars = 0      # Number of hex charatcers needed to display the address (byte number)
maxfilesize = 0   # Size of biggest file passed in
keepalive = False # Used to requiring input from the user before exiting the script


# Parse passed in arguments
for arg in sys.argv[1:]:
    argindex = sys.argv.index(arg)
    if(os.path.exists(arg) and os.path.isdir(arg) == False):
        paths.append(arg)
        displaynames.append(os.path.basename(arg))
        if os.path.getsize(arg) > maxfilesize : maxfilesize = os.path.getsize(arg)        
    else:
        if arg.__contains__("/?") or arg.__contains__("-h") or arg.__contains__("--help"): printhelp()
        if arg.isnumeric() : numbytes = int(arg) ; continue
        if arg.__contains__("-k") or arg.__contains__("/k"): keepalive = True ; sys.argv.remove(arg) ; continue
        invalidargs.append(arg)

# Display appropriate message, if needed.
if len(invalidargs) > 0  and len(paths) == 0: print("\nNo valid file given. If you gave a file, check your spelling, or try using absolute paths.") 
if len(sys.argv) == 1: printhelp()
 

# Make sure numbytes is not bigger then maxfilesize
if numbytes > maxfilesize : numbytes = maxfilesize


# Assign variable values that are based on arguments passed into this script
hexchars = len(str.format("{0:x}", numbytes - 1))
output = [""] * numbytes
outputhwidth = 14 + padding + hexchars


# Assing each columns' width to outputwidth, or displayname width, whichever is greater
# Padding is used to set space between each column
for name in displaynames:
    namewidth = len(name) + padding
    if namewidth > outputhwidth:
        columnwidths.append(namewidth)
    else: 
        columnwidths.append(outputhwidth)


# Go through each file, and read and format the first <numbytes> or <filesize> of data. Whichever is smaller.
# Paths and columnwidths have a direct correlation, so we can use path's index to get its relevant entry in columnwidths.  
for path in paths: 
    index = paths.index(path)
    with open(path, 'rb') as file:
        filesize = os.path.getsize(path)
        for byte in range(numbytes):
            currentbyte = file.read(1)
            outputstr = str.format(f'{{0:0>{hexchars}X}} ',byte)
            outputstr += str.format("{0:08b} {0:0>2X}", int.from_bytes(currentbyte))
            outputstr = outputstr.strip()
            outputstr = F"{outputstr} {currentbyte.decode(errors='ignore') if currentbyte.isalnum() else " "}"
            outputstr = str.format(f'{{0:<{columnwidths[index]}s}}',outputstr)
            output[byte] += outputstr


# Print output
print()
for name in displaynames:
    index = displaynames.index(name)
    print(str.format(f'{{0:<{columnwidths[index]}s}}', name), end="")
print("\n")
for row in output:
    print(row)
print()

if keepalive : print() ; input("Press enter to exit")
