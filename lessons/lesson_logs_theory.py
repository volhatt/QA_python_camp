"""
Хороший фреймвок имеет артефакт - директорию содержащую логи, видео, скриншоты, логи, результаты запросов,
разные snapshots from session storage, etc, downloads, info about created artefacts - eg. order id)

план.
1. Как создавать и записывать файлы.
2. Как парсить csv files
2. Как обращаться с path etc
2. как читать что у нас в папке, анализ файлов ( названия, размер итд )
3. Как создавать папки.
4. Как Это все сделать в pytest framework
"""

# how to crete file, read a file, write to the file
filename = 'testfile.txt'
path_to_file = f"/Users/okamene/src/QA_python_camp/lessons/{filename}"
mode = 'r'
mode = 'w'  # open a file for writing. If the file doesn’t exist, the open() function
# creates a new file. Otherwise, it’ll overwrite the contents of the existing file.
mode = 'x'  # open a file for exclusive creation. If the file exists, the open()
# function raises an error (FileExistsError). Otherwise, it’ll create the text file.

f = open(path_to_file, mode)
f.close()  # importand close always, this why we better use "with open"

with open('readme.txt', 'w') as f:
    f.write('Create a new text file!')  # create this file

# file with directory which doesn't exist - catch error or create folder first
with open('docs/readme.txt', 'w') as f:  # folder doc doesn't exist
    f.write('Create a new text file!')
#eg:
try:
    with open('docs/readme.txt', 'w') as f:
        f.write('Create a new text file!')
except FileNotFoundError:
    print("The 'docs' directory does not exist")

### 2. Как парсить csv files
"""
CSV is an acronym that stands for Comma Separated Values, CSV. 
A file in CSV format is just a text file that follows certain conventions. 
The CSV format says that values are going to be separated by 
commas and it says that every line of the file will have the same structure.
"""
# how to parse CSV file
"""
file could be like that
olympics.txt
"Name","Sex","Age","Team","Event","Medal"
"A Dijiang","M","24","China","Basketball","NA"
"Edgar Lindenau Aabye","M","34","Denmark/Sweden","Tug-Of-War","Gold"
"Christine Jacoba Aaftink","F","21","Netherlands","Speed Skating, 1500M","NA"
"""

fileconnection = open("olympics.txt", 'r')
lines = fileconnection.readlines()
header = lines[0]
field_names = header.strip().split(',')
print(field_names)
for row in lines[1:]:
    vals = row.strip().split(',')
    if vals[5] != "NA":
        print("{}: {}; {}".format(
                vals[0],
                vals[4],
                vals[5]))
fileconnection.close()
