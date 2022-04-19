# decorator


def copyright(func):
    def new_func():
        print("@ amamovsdfjkldjsakfljdskaljfkdsla")
        func()

    return new_func


@copyright
def smile():
    print("🙃")


@copyright
def angry():
    print("🤯")


@copyright
def love():
    print("🥰")


smile()
angry()
love()

def counter():
    i = 0
    def count():
        nonlocal i
        i += 1
        return i
    return count
c = counter()
for i in range(10):
    print(c(), end = ' ')