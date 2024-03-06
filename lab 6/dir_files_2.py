import os
path = input()
if(os.path.exists(f"{path}")):
    if(os.access(path, os.R_OK)):
        print("It is readable")
    else:
        print("It is not readable")
    if(os.access(path, os.W_OK)):
        print("It is writable")
    else:
        print("It is not writable")
    if(os.access(path, os.X_OK)):
        print("It is executable")
    else:
        print("It is not executable")
else:
    print("Path doesn't exist")