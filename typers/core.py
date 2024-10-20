from .Exceptions.validate_error import ValidateError

class Valid:
    # Not none
    @staticmethod
    def _not_none(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if value is None:
            raise ValueError(f"The '{name}' argument cannot be None.")

    # String
    @staticmethod
    def _string(value, name: str = None):
        if name == None:
            raise ValidateError("The 'name' argument must be a string : preferably the name of the relative function.")
        if not isinstance(value, str):
            raise ValueError(f"The '{name}' argument must be a string.")

    # Integers
    @staticmethod
    def _integer(value, name: str = None):
        if name == None:
            raise ValidateError("The 'name' argument must be a string : preferably the name of the relative function.")
        if not isinstance(value, int):
            raise ValueError(f"The '{name}' argument must be an integer.")

    @staticmethod
    def _positive_int_in(value, name: str = None):
        if name == None:
            raise ValidateError("The 'name' argument must be a string : preferably the name of the relative function.")
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"The '{name}' argument must be a positive integer.")

    @staticmethod
    def _positive_int_out(value, name: str = None):
        if name == None:
            raise ValidateError("The 'name' argument must be a string : preferably the name of the relative function.")
        if not isinstance(value, int) or value < 0:
            raise ValueError(f"The '{name}' argument must be a positive integer excluding 0.")


    @staticmethod
    def _negative_int_in(value, name: str = None):
        if name == None:
            raise ValidateError("The 'name' argument must be a string : preferably the name of the relative function.")
        if not isinstance(value, int) or value >= 0:
            raise ValueError(f"The '{name}' argument must be a negative integer.")

    @staticmethod
    def _negative_int_out(value, name: str = None):
        if name == None:
            raise ValidateError("The 'name' argument must be a string : preferably the name of the relative function.")
        if not isinstance(value, int) or value > 0:
            raise ValueError(f"The '{name}' argument must be a negative integer excluding 0.")

    # Floats
    @staticmethod
    def _float(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, float):
            raise ValueError(f"The '{name}' argument must be a float.")

    @staticmethod
    def _positive_float_in(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, float) or value <= 0:
            raise ValueError(f"The '{name}' argument must be a positive float.")

    @staticmethod
    def _positive_float_out(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, float) or value < 0:
            raise ValueError(f"The '{name}' argument must be a positive float excluding 0.")

    @staticmethod
    def _negative_float_in(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, float) or value >= 0:
            raise ValueError(f"The '{name}' argument must be a negative float.")

    @staticmethod
    def _negative_float_out(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, float) or value > 0:
            raise ValueError(f"The '{name}' argument must be a negative float excluding 0.")

    # Booleans
    @staticmethod
    def _boolean(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, bool):
            raise ValueError(f"The '{name}' argument must be a boolean.")

    # Lists
    @staticmethod
    def _list(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, list):
            raise ValueError(f"The '{name}' argument must be a list.")

    @staticmethod
    def _list_of_strings(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
            raise ValueError(f"The '{name}' argument must be a list of strings.")
    
    @staticmethod
    def _list_of_ints(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, list) or not all(isinstance(item, int) for item in value):
            raise ValueError(f"The '{name}' argument must be a list of integers.")

    @staticmethod
    def _list_of_floats(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, list) or not all(isinstance(item, float) for item in value):
            raise ValueError(f"The '{name}' argument must be a list of floats.")

    @staticmethod
    def _list_of_bools(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, list) or not all(isinstance(item, bool) for item in value):
            raise ValueError(f"The '{name}' argument must be a list of booleans.")
    
    # Ranges
    @staticmethod
    def _in_range(value, min_val, max_val, name: str = None):
        if min_val >= max_val:
            raise ValidateError("The 'min_val' argument cannot be bigger or equal to the 'max_val' argument.")
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, (int, float)) or not (min_val <= value <= max_val):
            raise ValueError(f"The '{name}' argument must be between {min_val} and {max_val}.")

    # Tuples
    @staticmethod
    def _tuple(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, tuple):
            raise ValueError(f"The '{name}' argument must be a tuple.")

    @staticmethod
    def _tuple_of_strings(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, tuple) or not all(isinstance(item, str) for item in value):
            raise ValueError(f"The '{name}' argument must be a tuple of strings.")

    @staticmethod
    def _tuple_of_ints(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, tuple) or not all(isinstance(item, int) for item in value):
            raise ValueError(f"The '{name}' argument must be a tuple of integers.")

    @staticmethod
    def _tuple_of_floats(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, tuple) or not all(isinstance(item, float) for item in value):
            raise ValueError(f"The '{name}' argument must be a tuple of floats.")

    @staticmethod
    def _tuple_of_bools(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, tuple) or not all(isinstance(item, bool) for item in value):
            raise ValueError(f"The '{name}' argument must be a tuple of booleans.")
