import os
path = input()
if(os.path.exists(f"{path}") and os.access(f"{path}", os.W_OK)):
    os.remove(path)
else:
    print("Path doesn't exist or you have no access")