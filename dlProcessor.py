from pyautogui import * 
import pyautogui 
import time 
import keyboard 
import random
import win32api, win32con
from tkinter import Tk
import os


class StartBot():
    script_dir=os.path.dirname(__file__)
    rootFolder=os.path.join(script_dir,"assets/")
    target=""
    
    
    def click(x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        
    
    def find(tg):
        try:
            coordinates= pyautogui.locateCenterOnScreen(StartBot.target+tg+".png",confidence=0.65)
            if coordinates:
                return True
        except pyautogui.ImageNotFoundException:
            return False
        
    def findClick(tg):
        try:
            coordinates= pyautogui.locateCenterOnScreen(StartBot.target+tg+".png",confidence=0.65)
            if coordinates:
                click(coordinates.x,coordinates.y)
                return True
        except pyautogui.ImageNotFoundException:
            return False
    def find2Click(tg):
        try:
            coordinates= pyautogui.locateCenterOnScreen(StartBot.target+tg+".png",confidence=0.65)
            if coordinates:
                click(coordinates.x,coordinates.y)
                time.sleep(3)
                click(coordinates.x,coordinates.y)
                return True
        except pyautogui.ImageNotFoundException:
            return False  
        
    def gameFlow():
        print("Gameflow")
        StartBot.findClick("AceptarBtn")
        if StartBot.find("TurnoText"):
            StartBot.find2Click("DrawCardImage")
            StartBot.findClick("CambioFaseBtn")
            StartBot.findClick("TerminarTurnoBtn")
            if StartBot.find("DescartaText"):
                StartBot.findClick("CartaDescartaBtn")
                StartBot.findClick("ConfirmarBtn")
    def resultsFlow():
        print("ResultsFlow")
        if StartBot.find("ResultsText"):
            StartBot.findClick("AceptarRecBtn")
            StartBot.findClick("NextBtn")
            
    def jcjFlow():
        print("JcJFlow")
        if StartBot.find("JcJText"):
            StartBot.findClick("DueloBtn")
            StartBot.findClick("DuelosIgualadosBtn")
    def ExFlow():
        if StartBot.find("ContinuarText"):
            StartBot.findClick("SiBtn")
    def mainMethod(res):
        StartBot.target=StartBot.rootFolder+res+"/"
        while keyboard.is_pressed('q') == False:
            StartBot.gameFlow()
            StartBot.resultsFlow()
            StartBot.jcjFlow()
            StartBot.findClick("EstadioJcJBtn")
            StartBot.ExFlow()
        print("bot stopped")
            


    
