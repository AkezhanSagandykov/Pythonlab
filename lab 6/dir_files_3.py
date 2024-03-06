import os
path = input()
if(os.path.exists(f"{path}")):
    print(os.path.basename(path))
    print(os.path.dirname(path))
else:
    print("Path doesn't exist")