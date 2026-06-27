class Developer:

    def __init__(self):
        self.name = "Aayush"
        self.role = "Future Software Developer"
        self.language = "Python"
        self.motto = "Learn, Build, Improve"

    def show_journey(self):
        print(" Developer:", self.name)
        print(" Goal:", self.role)
        print(" Favorite Language:", self.language)
        print("Motto:", self.motto)

    def inspiration(self):
        print("\nEvery developer starts with a single line of code.")
        print("Small programs today create big projects tomorrow 🚀")


dev = Developer()

dev.show_journey()
dev.inspiration()