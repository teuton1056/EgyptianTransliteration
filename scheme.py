class AmbiguousRequestError(Exception):
    pass

class Scheme:

    def __init__(self, name: str):
        self.name = name
        self.scheme = {}
        self.rev_scheme = {}

    def _register_char(self, src_char: str, dest_char: str):
        if src_char in self.scheme:
            raise AmbiguousRequestError("The char {} was already registered".format(src_char))
        self.scheme[src_char] = dest_char
        self.rev_scheme[dest_char] = src_char
        
    def exists(self, char: str) -> bool:
        return char in self.scheme

    def _convert_char(self, char: str) -> str:
        """
        Note that this function always returns a character, 
        even if the character is not registered in the scheme.
        This is important because we want to be able to convert
        strings with characters that are not in the scheme.
        """
        if char in self.scheme:
            return self.scheme[char]
        else:
            return char

    def _reverse_convert_char(self, char: str) -> str:
        """returns the character that maps to char in the scheme"""
        if char in self.rev_scheme:
            return self.rev_scheme[char]
        else:
            return char

    def convert(self, string: str, joiner="") -> str:
        """converts a string using the scheme
        uses the joiner to join the converted characters, 
        defaults to an empty string"""
        return joiner.join([self._convert_char(char) for char in string])


