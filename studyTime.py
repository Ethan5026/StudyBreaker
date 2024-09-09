from pydub import AudioSegment
from pydub.playback import play
from datetime import datetime, timedelta
import time
from pygame import mixer

import random 

def playSound(filePath):
    mixer.init()
    mixer.music.load(filePath)
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(3)
        
def startGame(selectedGames, breakTime):
    
    playSound('start.mp3')
    print("\n\nStart studying\n")
    
    time = datetime.now()
    time += timedelta(minutes=int(breakTime))
    
    print(f"Next break at {time.strftime("%I:%M %p")}")
    
    while(datetime.now() < time):
        continue
    
    selected_game = random.choice(selectedGames)
    print(f"Start your game: {selected_game[0]}")
    playSound(selected_game[1])
        
    input_str = 'barf'
    while(input_str != ''):
        input_str = input("Press Enter when you are finished with the game")
    
    startGame(selectedGames, breakTime)
        
        
def userManagement():
    
        
    print("Games are listed below:")
    games = [["Pitch", 'pitch.mp3'], ['Speed', 'speed.mp3'], ['Spot it', 'spotIt.mp3'], ['Golf', 'golf.mp3'], ['Nertz', 'nertz.mp3'], ['Go Fish', 'goFish.mp3'], ['Euchre', 'Euchre.mp3'], ['Rummy', 'rummy.mp3'], ['Cribbage', 'cribbage.mp3']]

    for game in games:
        print(game[0])
        
    excluded_input = input("\n\nInput the #'s of the games you wish to remove, seperated by spaces:  ")
    excluded_games = excluded_input.split(" ")
        
    selectedGames = []
    for i in range(len(games)):
        if not i in excluded_games:
            selectedGames.append(games[i])
            
    breakTime = input("\nSelect a time for your intermediary breaks:  ")
    
    startGame(selectedGames, breakTime)
    
if __name__ == '__main__':
    userManagement()
    
