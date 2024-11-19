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
    -> if the file doesn't exists then it returns FileNotFoundError
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

### Methods for reading a file
- read() -> reads an entire file as one string
- readlines() -> Reads an entire file as a list, where each item represents a line from the file
- readline() -> reads the next line
- Additionally, we can read files using 'for' statement iterating through each line.


## WORKING WITH CSV FILES
- CSV (Comma-Separated Values) is a most common text file type.
- In the CSV file, each row is called a record (instance).
- In the CSV file, each row has one to many column, and each column is separted by comma (,).

### Sample csv file
name,age,dept,city,salary
anil,35,hr,hyd,48000.0
kumar,44,management,hyd,80000.0
umesh,29,it,che,45000.0
kiran,36,hr,del,55000.0

### Use 'csv' module to work with CSV files
- First, import the `csv` module
- Use 'writer()' function from csv module to create CSV writer object. Then use 'writerows()' method to write data to a csv file through CSV object.
- Use 'reader()' function to create CSV reader object. And then you can loop through each line.


## WORKIGN WITH BINARY FILES
> All non-text files are called binary file. And the data in the binary files is a sequence of bytes.

