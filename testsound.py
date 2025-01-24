
import pygame
from gtts import gTTS

language = 'en'

def speak(audio):
    # Convert text to speech
    myobj = gTTS(text=audio, lang=language, slow=False)
    myobj.save("welcome.mp3")
    
    # Initialize pygame mixer
    pygame.mixer.init()
    
    # Load and play the audio file
    try:
        pygame.mixer.music.load("welcome.mp3")
        pygame.mixer.music.play()
        
        # Wait for the sound to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        print('Playing sound using pygame.mixer')
    except Exception as e:
        print(f"Error playing sound: {e}")
    finally:
        pygame.mixer.quit()  # Clean up pygame mixer

# Example usage
speak("Hello, this is a test message.")
