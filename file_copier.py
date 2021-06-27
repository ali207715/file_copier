"""
Problem 1: copying files.
Libraries used: shutil; copyfile function

NOTE: As the program is fairly elementary, not a lot of comments are present.
      Also, please do make sure to include the extension of the file to be copied.
"""

import shutil

with open("config.xml", "r") as config_file:  # Reading the file (xml format)
    data = config_file.readlines()
    for no_of_line, line in enumerate(data):
        if "<file" in line:
            source_path = data[no_of_line + 1][25:-2]
            destination_path = data[no_of_line + 2][30:-2]
            file_name = data[no_of_line + 3][23:-2]
            shutil.copyfile(source_path+"/"+file_name, destination_path+"/"+file_name)


