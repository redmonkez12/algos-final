greetings = []


def greeter(func):
    print(f"running greeter({func})")
    greetings.append(func)
    return func
