from src.gui import GUI
from src.systemData import SystemData
from src.threadController import ThreadController

def main():
    systemData = SystemData()
    threadController = ThreadController()
    app = GUI(systemData, threadController)


    app.run()

if __name__ == "__main__":
    main()
