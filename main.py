from src.gui import GUI
from src.systemData import SystemData

def main():
    sysData = SystemData()
    app = GUI(sysData)


    app.run()

if __name__ == "__main__":
    main()
