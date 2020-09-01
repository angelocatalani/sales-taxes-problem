class MalformedBasketError(RuntimeError):
    """
    The Baskets strings are malformed.
    """

    def __init__(self, message: str):
        """
        Initialize the MessageError exception.

        :param message: the error message
        """

        super().__init__(message)
