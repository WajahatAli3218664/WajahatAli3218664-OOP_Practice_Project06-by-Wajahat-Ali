#Function Decorators
#Assignment 16:

#Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().

def log_function_call(func):
    """
    🛠️ Decorator to log before function execution.
    
    Prints a message before calling the actual function.
    
    Args:
        func (function): The function to wrap.
    
    Returns:
        function: The wrapped function.
    """
    def wrapper():
        print("🚀 Function is being called")
        func()
    return wrapper

@log_function_call
def say_hello():
    """
    👋 A simple function that says hello.
    """
    print("👋 Hello, World!")

# 🚀 Example usage
if __name__ == "__main__":
    say_hello()
