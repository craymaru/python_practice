import time
import pyautogui as pgui
from AppKit import NSWorkspace

workspace = NSWorkspace.sharedWorkspace()
target_app_names = ["PS4リモートプレイ"]


def checkWindow():
    app_names = workspace.activeApplication()["NSApplicationName"]
    if app_names in target_app_names:
        return True
    else:
        return False


while True:
    if checkWindow():
        pgui.typewrite(["enter"])
        print("enter")
    time.sleep(0.25)