import time
import pyautogui as pgui
from AppKit import NSWorkspace

workspace = NSWorkspace.sharedWorkspace()


def checkWindow():
    app_names = workspace.activeApplication()["NSApplicationName"]
    if app_names in ["PS4リモートプレイ"]:
        return True
    else:
        return False


def detectPos(path):

    pos = pgui.locateCenterOnScreen(path, region=(1530, 350, 100, 100), confidence=0.950)
    print(path, pos)
    return pos


def skipExecute(path):

    pos = pgui.locateCenterOnScreen(path, region=(850, 1100, 100, 100), confidence=0.950)
    print(path, pos)

    if pos:
        pgui.typewrite(["enter"])
        print("enter")
        time.sleep(0.05)


def pressEnter():
    for i in range(10):
        pgui.typewrite(["enter"])
        print("enter")
        time.sleep(0.05)
    time.sleep(1.0)


while True:
    time.sleep(0.1)

    if checkWindow():
        for i in range(20):
            if detectPos("d3/normal.png"):
                pressEnter()
            elif detectPos("d3/ancient.png"):
                pressEnter()
                pass
            elif detectPos("d3/primal.png"):
                exit()
        skipExecute("d3/execute.png")

        # if detectPos("./d3/primal.png"):
        #     break
        # else:

        #     for i in range(6):
        #         pgui.typewrite(["enter"])
        #         print("enter")
        #         time.sleep(0.2)
        # time.sleep(.5)
