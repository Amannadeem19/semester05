class CalApp:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def div(self):
        return self.a / self.b

    def mult(self):
        return self.a * self.b


if __name__ == '__main__':

    a = int(input("enter first number"))
    b = int(input("enter second number"))
    obj = CalApp(a, b)

    choice = 1

    while choice != 0:
        print("1. add")
        print("2. sub")
        print("3. divide")
        print("4. Multiply")
        choice = int(input("Enter your choice"))
        if choice == 1:
            print("Result : ", obj.add())
        elif choice == 2:
            print("Result : ", obj.sub())

        elif choice == 3:
            print("Result : ", obj.div())

        elif choice == 4:
            print("Result : ", obj.mult())
