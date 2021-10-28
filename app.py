from pygame import *

init()
presets = False
settings = False
run = True
sliderX = 50
sliderY = 52
mainText = font.Font("freesansbold.ttf", 15)
x = 500
y = 400
bgColor = "white"
screen = display.set_mode((x,y))
icon = image.load("scroll.png")
image1 = image.load("product.jpg")
title = "Easy Sliding"
display.set_icon(icon)
display.set_caption(title)

def showText(font, text, x, y, color1 ,color2 ,color3):
    txt = font.render(text, True, (color1,color2,color3)) 
    screen.blit(txt, (x,y))

def slideLong(x,y):
    global sliderX
    longPart = draw.rect(screen, (0,0,0), Rect(x,y,400,8), border_radius = 15)
    longPart1 = draw.rect(screen, (0,191,255), Rect(x,y,sliderX-x,8), border_radius = 15)
    return longPart


def slideShort(x,y):
    shortPart = draw.circle(screen, (0,0,0), (x,y),15)
    return shortPart

def showBg(icon):
    screen.blit(icon, (0,0))

def drawButton(x, y, width, height, color1, color2, color3, cText1,cText2,cText3, text):
    object = Rect(x,y,width,height)
    button = draw.rect(screen, (color1,color2,color3), object)
    sizeX = mainText.size(text)[0]
    sizeY = mainText.size(text)[1]
    showText(mainText, text, x+(width/2)-(sizeX/2), y+(height/2)-(sizeY/2), cText1, cText2, cText3)
    return button

def app():
    global appli
    global presets
    global settings
    global run

    presets = False
    settings = False
    while run:
        screen.blit(image1, (0,0))
        slider = drawButton(20,20,130,40,0,0,0,255,255,255, "Slider Presets")
        setting = drawButton(20,80,130,40,0,0,0,255,255,255, "Settings")

        mouseX,mouseY = mouse.get_pos()

        if (slider.collidepoint(mouseX,mouseY)):
            slider = drawButton(15,15,135,45,0,0,0,255,255,255, "Slider Presets")
        if (setting.collidepoint(mouseX,mouseY)):
            setting = drawButton(15,75,135,45,0,0,0,255,255,255, "Settings")

        for e in event.get():
            if e.type == QUIT:
                run = False
            
            if e.type == MOUSEBUTTONDOWN:
                if (e.button == 1 and slider.collidepoint(mouseX,mouseY)):
                    presets = True
                    Presets()
                if (e.button == 1 and setting.collidepoint(mouseX,mouseY)):
                    settings = True
                    Settings()
        display.update()

def Presets():
    global presets
    global run
    global settings
    global sliderY
    global sliderX

    run = False
    settings = False
    while presets:
        screen.fill("white")
        longPart = slideLong(50,50)
        shortPart = slideShort(sliderX,sliderY)

        mouseX, mouseY = mouse.get_pos()

        sensitivity = drawButton(400,70,100,15,255,255,255,0,0,0,str(sliderX-50))
        goBack = drawButton(20,350,130,40,0,0,0,255,255,255, "Main Menu")

        if (goBack.collidepoint(mouseX,mouseY)):
            goBack = drawButton(15,345,135,45,0,0,0,255,255,255, "Main Menu")

        for e in event.get():
            if e.type == QUIT:
                presets = False
            
            if e.type == MOUSEBUTTONDOWN:
                if (e.button == 1 and longPart.collidepoint(mouseX, mouseY)):
                    while (sliderX != mouseX):
                        if (sliderX < mouseX):
                            sliderX += 1
                        elif (sliderX > mouseX):
                            sliderX -= 1
                        if (sliderX < 5):
                            sliderX = 0
                        elif (sliderX > 395):
                            sliderX = 400
                        shortPart = slideShort(sliderX,sliderY)
                
                if (e.button == 1 and goBack.collidepoint(mouseX,mouseY)):
                    run = True
                    app()
        display.update()


def Settings():
    global presets
    global run
    global settings

    presets = False
    run = False
    while settings:
        screen.fill("white")
        goBack = drawButton(20,350,130,40,0,0,0,255,255,255, "Main Menu")
        mouseX,mouseY = mouse.get_pos()

        if (goBack.collidepoint(mouseX,mouseY)):
            goBack = drawButton(15,345,135,45,0,0,0,255,255,255, "Main Menu")
        for e in event.get():
            if e.type == QUIT:
                settings = False
            if e.type == MOUSEBUTTONDOWN:
                if (e.button == 1 and goBack.collidepoint(mouseX,mouseY)):
                    run = True
                    app()

        display.update()

while (run == True or presets == True or settings == True):
    if (run == True and presets == False and settings == False):
        app()
    if (run == False and presets == True and settings == False):
        Presets()
    if (run == False and presets == False and settings == True):
        app()
if (run == False and presets == False and settings == False):
    quit()