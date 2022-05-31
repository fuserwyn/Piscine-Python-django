class Intern:

    def __init__(self, Name = None):
        self.Name = "My name? I’m nobody, an intern, I have no name." if Name is None else Name
        
    def __str__(self):
        return self.Name
    
    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self) -> Coffee():
        return Intern.Coffee()


def test():
    vasya = Intern("Vasya")
    print(vasya)
    try:
        print(vasya)
        print(vasya.make_coffee())
        print(vasya)
        print(vasya.make_coffee())
        vasya.work()
        print(vasya.make_coffee())
    except Exception:
        print("bad")
    print(vasya.make_coffee())

if __name__ == '__main__':
    test()