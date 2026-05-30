from src.gui import GUI
from src.controller import Controller

def main():
    controller = Controller()
    app = GUI(controller)


    app.run()

if __name__ == "__main__":
    main()
