class MalformedReceiptError(RuntimeError):
    """
    The input Receipt is not well formatted.
    """

    def __init__(self, message: str):
        """
        Initialize the MessageError exception.

        :param message: the error message
        """

        super().__init__(message)
