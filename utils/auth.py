import re


def valid_email(email: str) -> bool:
    """
    Checks if the given email is valid.

    Args:
        email (str): The email to be checked.

    Returns:
        bool: True if the email is valid, False otherwise.

    """
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None
