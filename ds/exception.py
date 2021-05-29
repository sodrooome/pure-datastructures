class ThrowException(Exception):
    pass


class DsIndexError(ThrowException):
    """Exception for handler when index of Stack, List, Queue is empty."""

    def __init__(self):
        super().__init__("Stack / List / Queue is empty, set a value first.")


class DsPeekIndexError(ThrowException):
    """Exception for handler when peeking an object is None."""

    def __init__(self):
        super().__init__(
            "Stack / List / Queue is empty, you either must be popped or not set a value."
        )


class DsValueError(ThrowException):
    """Exception for indicates that data-type or value is not correct."""

    def __init__(self):
        super().__init__(
            "Value error, either your argument or inputted value is not correct."
        )
