import math

def add(x, y):
    try:
        if isinstance(x, int) and isinstance(y, int):
            return x + y

        try: 
            x = int(x)
            y = int(y)
            return x + y

        except:
            print("Not a decimal or int")

        x = str(x)

        if 'b' in x:
            x = inputLogic(x, 2)
            return x + y
        if 'x' in x:
            x = inputLogic(x, 16)
            return x + y

        if 'o' in x:
            x = inputLogic(x, 8)
            return x + y

    
    except:
        print("Inputted incorrectly")


def subtract(x, y):
    try:
        if isinstance(x, int) and isinstance(y, int):
            return x - y

        try: 
            x = int(x)
            y = int(y)
            return x - y

        except:
            print("Not a decimal or int")

        x = str(x)

        if 'b' in x:
            x = inputLogic(x, 2)
            return x - y
        if 'x' in x:
            x = inputLogic(x, 16)
            return x - y

        if 'o' in x:
            x = inputLogic(x, 8)
            return x - y

    
    except:
        print("Inputted incorrectly")

def multi(x, y):
    return x * y
    try:
        if isinstance(x, int) and isinstance(y, int):
            return x * y

        try: 
            x = int(x)
            y = int(y)
            return x * y

        except:
            print("Not a decimal or int")

        x = str(x)

        if 'b' in x:
            x = inputLogic(x, 2)
            return x * y
        if 'x' in x:
            x = inputLogic(x, 16)
            return x * y

        if 'o' in x:
            x = inputLogic(x, 8)
            return x * y

    
    except:
        print("Inputted incorrectly")

def div(x, y):
    return x / y
    try:
        if isinstance(x, int) and isinstance(y, int):
            return x / y

        try: 
            x = int(x)
            y = int(y)
            return x / y

        except:
            print("Not a decimal or int")

        x = str(x)

        if 'b' in x:
            x = inputLogic(x, 2)
            return x / y
        if 'x' in x:
            x = inputLogic(x, 16)
            return x / y

        if 'o' in x:
            x = inputLogic(x, 8)
            return x / y

    
    except:
        print("Inputted incorrectly")

def root(x, y):
    try:
        if isinstance(x, int) and isinstance(y, int):
            return math.sqrt(x), math.sqrt(y);

        try: 
            x = int(x)
            return math.sqrt(x), math.sqrt(y);

        except:
            print("Not a decimal or int")

        x = str(x)

        if 'b' in x:
            x = inputLogic(x, 2)
            return math.sqrt(x), math.sqrt(y);
        if 'x' in x:
            x = inputLogic(x, 16)
            return math.sqrt(x), math.sqrt(y);

        if 'o' in x:
            x = inputLogic(x, 8)
            return math.sqrt(x), math.sqrt(y);

    
    except:
        print("Inputted incorrectly")

def exp(x, y):
    return x ** y
    try:
        if isinstance(x, int) and isinstance(y, int):
            return x ** y

        try: 
            x = int(x)
            y = int(y)
            return x ** y

        except:
            print("Not a decimal or int")

        x = str(x)

        if 'b' in x:
            x = inputLogic(x, 2)
            return x ** y
        if 'x' in x:
            x = inputLogic(x, 16)
            return x ** y

        if 'o' in x:
            x = inputLogic(x, 8)
            return x ** y

    
    except:
        print("Inputted incorrectly")


def inputLogic(x, y):
    return int(x, base=y)

