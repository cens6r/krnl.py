class Error(Exception):
    """Base Class Exception"""
    pass

class InvalidDLLError(Error):
    """Raised when the provided DLL is invalid"""
    pass
