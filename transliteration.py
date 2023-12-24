from scheme import Scheme, AmbiguousRequestError
import os

def load_scheme(name: str) -> Scheme:
    """loads a scheme from a file"
    TODO: On linux/mac check ~/.config/?? for the file but on windows check some 
    appropriate directory
    """
    # check if the file is located in the same directory as this file
    # if not, check for a schemes/ directory or a .schemes/ directory
    if os.path.isfile(name + ".scheme"):
        pass 
    elif os.path.isfile(os.path.join("schemes", name + ".scheme")):
        name = os.path.join("schemes", name)
    elif os.path.isfile(os.path.join(".schemes", name + ".scheme")):
        name = os.path.join(".schemes", name)
    else:
        raise FileExistsError("The scheme {} does not exist".format(name))
    with open(name + ".scheme", 'r') as f:
        scheme = Scheme(name)
        lines = f.readlines()
        for line in lines:
            src_char, dest_char = line.split('|')
            scheme._register_char(src_char.lstrip(), dest_char.strip())
        return scheme