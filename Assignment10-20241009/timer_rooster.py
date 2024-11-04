import time
import pygame    #playsound doesnt work with new version so pygame


def countdown_timer(seconds):
    while seconds > 0:
        mins = int(seconds / 60)
        secs = int(seconds % 60)
        timer = f'{mins}:{secs:02}'
         
        print(timer)
        time.sleep(1)  
        seconds -= 1   
    print("Time's up!")
    
    pygame.mixer.init()  # Initialize Pygame Mixer
    sound_file = r"C:\python\New folder\rooster.wav"  # Define the sound file path(use r for raw or use double backslash)
    sound = pygame.mixer.Sound(sound_file)  # Load the sound file
    sound.play()  # Play the sound
    while pygame.mixer.get_busy():  # Keep the program running until the sound finishes
        pygame.time.Clock().tick(10)

seconds = int(input("Enter the time in seconds: "))  

countdown_timer(seconds)
