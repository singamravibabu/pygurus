# WORKING WITH FILES
There are two types of files: text & binary

## TEXT FILES
Any file that contains characters and each line ends with new line (\n) character is a text file
Text file examples: .txt, .csv, .json, .html, .xml

## BINARY FILES
Any non-text file
It is a sequence of bytes and may contain some text portions
Examples: .exe, .msi, .zip, image files, vidoe files, audio file, database file, etc

## FILE OPERATIONS
1. Open a File
2. Read from the file or write to the File
3. Close the file

### OPENING A FILE: built-in open() function
Syntax:
    open(file_name, mode)
        * creates/returns a file object
        * file_name: filepath, filename, and file extension
        * mode: read, write, append, binary

### MODES OF OPENING A FILE:
'r' - read mode
    -> reads an existing file
    -> if the file not found then it returns FileNotFoundError
'w' - write mode
    -> if the file doesn't exists it creates a new file
    -> if the file already exists, then it overwrites the content
'a' - append mode
    -> if the file doesn't exits it creates a new file
    -> if the file already exists, it appends the data to it
'b' - binary mode
    -> to work with binary files
    -> always use with read and write modes: 'rb' and 'wb'


### CLOSING A FILE
Use the close method to close a file
file_object.close()