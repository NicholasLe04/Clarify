from api import get_new_code, highlight_diff
from args import get_args

def clarify():
    file_path = get_args().file_path

    if file_path == './':
        print("No file path given")
        exit()

    old_code, new_code = get_new_code(file_path)

    print(f""" 
\033[1m
Revised Code 
--------------------------------------------------------------
\033[0;0m
{highlight_diff(old_code, new_code)}

\033[1m--------------------------------------------------------------\033[0;0m
""")


    confirmation = None
    while confirmation != 'y' and confirmation != 'n':
        confirmation = input("Is this code suitable to be saved into the original file? (Y/N)\n").lower()

    if confirmation == 'y':
        file = open(file_path, "w")
        file.writelines(new_code)
        file.close()
        print(f"New code has been saved to \"{file_path}\"")
    else:
        print("GG")
