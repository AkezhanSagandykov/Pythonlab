import os
with open("Copy.txt", 'w') as file:
    file.write("Paul McCartney, John Lennon, Freddie Mercury, Michael Jackson, Chester Bennington")
with open("Copy.txt", 'r') as file:
    data = file.read()
with open("Paste.txt", 'a') as file:
    file.write(data)