class DuplicateError(Exception):

    def __init__(self, message: str, *args, **kwargs) -> None:
        super().__init__(message, *args, **kwargs)
