import functools

def note(sunc):
    "note function"
    @functools.wraps(sunc)
    def wrapper():
        "wrapper function"
        print("note somethion")
        return sunc
    return wrapper

@note
def test():
    "test function"
    print("func")

test()
print(test.__doc__)


