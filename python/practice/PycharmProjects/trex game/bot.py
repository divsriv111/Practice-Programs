from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

#class containing set of all cordinates
#I have collected all the cordinate by taking ss and then using paint.net
class Cordinates():
    #cordinate of replay button (mid)
    replayBtn = (340,390)

    #cordinate of dinosaur's top right head pixel
    dinosaur = (171,395) #original was (171,395), adding the difference of original and duck(42)

    # x = 240 for tree obstacle
    # y = 420 for smaller obstacle


def restartGame():
    # pyautogui has one line code to click anywhere on the screen
    # this will restart  if clicked anywhere, automatically
    pyautogui.click(Cordinates.replayBtn)
    # when the game will start, it will press down button
    pyautogui.keyDown('down')


def pressSpace():
    # function for space button (jump)
    # automatically jumps for whatever times it is called
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    print('Jump')
    time.sleep(0.18)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')

def imageGrab():
    # This function detects any obstacle coming to the way of dinosaur
    box = (Cordinates.dinosaur[0]+60, Cordinates.dinosaur[1],
           Cordinates.dinosaur[0]+100, Cordinates.dinosaur[1]+30)
    image = ImageGrab.grab(box)
    greyImage = ImageOps.grayscale(image)
    a = array(greyImage.getcolors())
    print(a.sum())
    return a.sum()

def main():
    restartGame()
    while True:
        if(imageGrab()!=1447):
            pressSpace()
            time.sleep(0.1)

main()
###### STEP-1 ######
# note the restart button position
# note the cordinate for dianosaur's top right head
# implement restartgame automatic button
# implement press space button

###### STEP-2 ######
# decide the point where the dinosaur should jump before obstacle
# find cordinate of the point using paint.net
# repeat the process for smaller obstacle and note the points
# make box function so that our program can understand and can jump if it realizes box is coming
# box = (x1,y1,x2,y2)
# box = (dinoCord.X + distance, dinoCord.Y, dinoCord.X + distance + 40, dinoCord.Y + 30)

# any image is much more efficient to analyze in greyscale scheme
# so we will comvert all the images that is being caputed in greyscale and covert it into numpy arrays
# we can see by removing return startment in imagegrab() by print(a.sum()) that if there is no tree, the sum is 1447
# define main function

###### STEP-3 ######
# Take screenshot of duck being ducked down
# open it into paint.net and not the cordinate of duck's top y-axis, it comes out to be 437
# note that the difference between original duck and down duck is 42
# update box size and new blank screen sum
