# combine the following functions into single python file:
### 1) search a list of files for a text string
### 2) kick out a file with the list of filenames that have the text of interest 
### 3) if string is present, run the .json-to-.csv conversion and append contents of json file to a single csv file

### import modules
import pandas as pd
import os
import pathlib
from pathlib import Path
import json

### search a list of files for a text string
# Ask the user to enter string to search
search_path = input("Enter directory path to search (for best results include trailing slash at end of directory path): ")
file_type = input("File Type (e.g. .json) : ")
search_str = input("Enter the search string (e.g. Dimmig) : ")

# Append a directory separator if not already present
# Note - this works for Mac and -nix, would need to make '\' for Windows pathing
if not (search_path.endswith("/") or search_path.endswith("\\") ): 
        search_path = search_path + "/"
 
# If path does not exist, set search path to current directory
# Again - will need to tweak for Windows
if not os.path.exists(search_path):
        search_path ="./"

# Repeat for each file in the directory  
for fname in os.listdir(path=search_path):
   # Apply file type filter   
   if fname.endswith(file_type):
        # Open file for reading
        fo = open(search_path + fname)
        # Read the first line from the file
        line = fo.readline()
        # Initialize counter for line number
        line_no = 1
        # Loop until EOF
        while line != '' :
                # Search for string in line
                index = line.find(search_str)
                if ( index != -1) :
                    # if you want to display to screen the text containing the search string, un-comment the following line
                    # print(fname, "[", line_no, ",", index, "] ", line, sep="")

                    # create/append a file with filenames of those with the search string of interest 
                    file1 = open(search_path + "filelist.txt", "a")  # append mode
                    file1.write(fname + "\n")
                    file1.close()

                    # create/append contents of the .json files with the search string into a csv file

                    # set path to file
                    fullpath = search_path + fname
                    fullpath_str = str(fullpath)
                    p = Path(fullpath_str)

                    # read json
                    with p.open('r', encoding='utf-8') as f:
                        data = json.loads(f.read())

                    # create dataframe
                    df = pd.json_normalize(data)

                    ##### will instead appeand to existing file but also make sure header is
                    ##### printed at the first write if file doesn't exist yet
                    output_path=search_path + 'text_to_spreadsheet_output.csv'
                    df.to_csv(output_path, mode='a', header=not os.path.exists(output_path))



                # Read next line
                line = fo.readline()
                
                # Increment line counter
                line_no += 1

        # Close the files
        fo.close()
    
print("\nfilelist.txt has been created in the search path you entered. \n")
print ("text_to_spreadsheet_output.csv has been created in the search path you entered. \n")
k=input("press close to exit")




