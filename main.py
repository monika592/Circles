def to_upper(name):
    return name.upper();
def say_hello(name):
    print("hello",name)

if __name__ == "__main__":
    name = "monika"
    say_hello(name)
    up = to_upper(name)
    say_hello(up)