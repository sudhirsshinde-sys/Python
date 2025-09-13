# Sample Python script for testing file transfer and Git commit

def greet(name: str) -> str:
    """Return a greeting message for the provided name."""
    return f"Hello, {name}! Welcome to your WSL environment."


if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
