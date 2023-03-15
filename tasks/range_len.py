# Online Python - IDE, Editor, Compiler, Interpreter
names = ['John Smith', 'Onika Nicuarga', 'will James']


def check_name(name):
    """
    Print True if name is capitalized correctly,
    False if otherwise
    """

    print(not False in [word[0].isupper() for word in name.split(" ")])


for name in names:
    check_name(name)

print("this is an error:")

print(3/0)
