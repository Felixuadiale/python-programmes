def check_password_strength(password):
    """
    Checks the strength of a password based on several criteria.

    Args:
        password (str): The password to check.

    Returns:
        str: A message indicating the password strength.
    """
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    if not re.search(r"[a-z]", password):
        return "Weak: Password must contain at least one lowercase letter."
    if not re.search(r"[A-Z]", password):
        return "Weak: Password must contain at least one uppercase letter."
    if not re.search(r"\d", password):
        return "Weak: Password must contain at least one digit."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Password must contain at least one special character."
    if re.search(r"\s", password):
    return "Medium: Avoid spaces in your password."
    return "Strong: This is a good password."


password = input("Enter your password: ")
strength = check_password_strength(password)
print(strength)