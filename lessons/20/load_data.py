def load(filename:str) -> int:
    try:
        reader = open(filename, 'r')
        num = int(reader.read())
        reader.close()
        return num
    except FileNotFoundError:
        return -1
    except ValueError:
        return 0
    