try:
    open("config.txt")
except OSError as err:
    if err.errno == 2:
        print("El archivo no existe")
        print("Couldn't find the config.txt file!")
    elif err.errno == 13:
        print("Found config.txt but couldn't read it")
    else:
        print("Something else went wrong")