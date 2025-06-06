import pygame
import pyttsx3
import speech_recognition as sr


def text_to_speech(text):
    # Initialize the text-to-speech engine
    # text = text+".    Now it's your turn"
    engine = pyttsx3.init()

    # Get the list of available voices
    voices = engine.getProperty('voices')

    # Set a female voice (index may vary depending on your system)
    engine.setProperty('voice', voices[1].id)  # Index 1 might be a female voice, but this depends on your system
    engine.setProperty('pitch', 0.1)
    engine.setProperty('volume',1) # between 0.0 to 1.0
    engine.setProperty('rate',135) #speed of voice

    # Convert text to speech
    engine.save_to_file(text, './general_legal_awareness\tts_output.wav')  # You can change the format to 'wav' if desired

    # Close the engine
    engine.runAndWait()


# def hin_text_to_speech(text, language='hi'):
#     # Initialize the text-to-speech engine
#     engine = pyttsx3.init()

#     # Set the language (Hindi in this case)
#     engine.setProperty('rate', 150)  # You can adjust the speed (words per minute)
#     engine.setProperty('volume', 1)  # You can adjust the volume (0.0 to 1.0)

#     # Set the language for the speech
#     engine.setProperty('voice', f'hindi/{language}')

#     # Convert the text to speech
#     engine.say(text)

#     # Wait for the speech to finish
#     engine.runAndWait()





text1 = '''
    This is your general rights.
    Reservation quota:
        The Act mandates a reservation of at least, 4 percent of total vacancies in government establishments for PWDs.

    Non-Discrimination:
        Employers are prohibited from discriminating against PWDs in hiring, promotion, and job retention.

    Reasonable Accommodation:
        Employers must provide reasonable accommodations to facilitate the work environment for PWDs.

    Accessibility:
        Workplaces should be made accessible, and employers are required to provide assistive devices as needed.

    Equal Opportunities:
        PWDs should have equal opportunities for career advancement and training programs.
    
    Awareness and Sensitization:
        Employers are encouraged to promote awareness and sensitize employees about working with PWDs.

    Quotes:
        Various government schemes and incentives exist to promote employment and entrepreneurship among PWDs.

    Legal Remedies:
        Legal remedies are available for PWDs facing discrimination, including filing complaints with the appropriate authorities

    Corporate Social Responsibility (CSR):
        Companies are encouraged to include initiatives for PWDs as part of their CSR activities.
'''

text2 = '''
आरक्षण कोटा:

अधिनियम दिव्यांगों के लिए सरकारी प्रतिष्ठानों में कुल रिक्तियों में से कम से कम 4% आरक्षण अनिवार्य करता है।

• गैर भेदभाव:

नियोक्ताओं को नियुक्ति, पदोन्नति और नौकरी बरकरार रखने में दिव्यांगों के साथ भेदभाव करने से प्रतिबंधित किया गया है।

उचित आवास:

नियोक्ताओं को विकलांग व्यक्तियों के लिए कार्य वातावरण को सुविधाजनक बनाने के लिए उचित आवास प्रदान करना चाहिए।

• अभिगम्यता:

कार्यस्थलों को सुलभ बनाया जाना चाहिए, और नियोक्ताओं को आवश्यकतानुसार सहायक उपकरण प्रदान करना आवश्यक है।

• समान अवसर:

दिव्यांगों को करियर में उन्नति और प्रशिक्षण कार्यक्रमों के लिए समान अवसर मिलने चाहिए।

कानूनी ज्ञान जागरूकता

• जागरूकता और संवेदनशीलता:

नियोक्ताओं को विकलांग व्यक्तियों के साथ काम करने के बारे में जागरूकता को बढ़ावा देने और कर्मचारियों को संवेदनशील बनाने के लिए प्रोत्साहित किया जाता है।

• उद्धरण:

दिव्यांगों के बीच रोजगार और उद्यमशीलता को बढ़ावा देने के लिए विभिन्न सरकारी योजनाएं और प्रोत्साहन मौजूद हैं।

• कानूनी उपायों:

भेदभाव का सामना करने वाले दिव्यांगों के लिए कानूनी उपाय उपलब्ध हैं, जिनमें उपयुक्त प्राधिकारियों के पास शिकायत दर्ज करना भी शामिल है

• कॉर्पोरेट सामाजिक उत्तरदायित्व (सीएसआर):

कंपनियों को अपनी सीएसआर गतिविधियों के हिस्से के रूप में दिव्यांगों के लिए पहल शामिल करने के लिए प्रोत्साहित किया जाता है
'''





pygame.init()

frame1 = "./assets/frame1.png"
image1 = pygame.image.load(frame1)

# Get the dimensions of the screen
screen_info = pygame.display.Info()
width, height = screen_info.current_w, screen_info.current_h

pygame.font.init()
font = pygame.font.Font(None, 50)
clock = pygame.time.Clock()
# Set up display (use FULLSCREEN flag)
screen = pygame.display.set_mode((1900, 800), pygame.FULLSCREEN)

# Colors
black = (0, 0, 0)
white = (255,255,255)
gray =  (200,200,200)



# Define class button
class Button:
    def __init__(self, x, y, width, height, bcolor, text, tcolor, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.bcolor = bcolor
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.action = action
        self.visible = True
        self.tcolor = tcolor
        self.is_pressed = False

    def draw(self, screen):
        if self.visible:
            pygame.draw.rect(screen, self.bcolor, self.rect)
            text_surface = self.font.render(self.text, True, self.tcolor)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)




def main():
    screen_info = pygame.display.Info()
    width, height = screen_info.current_w, screen_info.current_h


    # Close button properties (moved to top right)
    close_button = Button(1808, 30, 55, 55, 'red', 'X', white, 'close_button')
    toggle_button = Button(900,30,55,55,'red', 'x', white, 'toggle')

    text_to_speech(text1)

    pygame.mixer.init()
    # pygame.mixer.music.load('tts_output.wav')

    cnt=0

    text_to_speech(text1)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if close_button.rect.collidepoint(event.pos):
                    done = True
                # if toggle_button.rect.collidepoint(event.pos):
                #     toggle_button.is_pressed = not toggle_button.is_pressed

            # if event.type==pygame.KEYDOWN:        
            #     if event.key==pygame.K_p:
                if cnt==0:
                    if not toggle_button.is_pressed:
                        text_to_speech(text1)
                        pygame.mixer.music.load('tts_output.wav')
                        pygame.mixer.music.play()
                    # if toggle_button.is_pressed:
                    #     hin_text_to_speech(text2)
                    cnt=1
                    # pygame.mixer.music.load('tts_output.wav')
                    # pygame.mixer.music.play()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_r:
                    if not toggle_button.is_pressed:
                        text_to_speech(text2)
                        pygame.mixer.music.load('tts_output.wav')
                        pygame.mixer.music.play()
                    # if toggle_button.is_pressed:
                    #     hin_text_to_speech(text2)
                    # pygame.mixer.music.load('tts_output.wav')
                    # pygame.mixer.music.play()
        screen.fill(white)
        if not toggle_button.is_pressed:
            screen.blit(image1,(0,0))
        elif toggle_button.is_pressed:
            screen.fill(black)
            pygame.display.flip()
        # toggle_button.draw(screen)
        close_button.draw(screen)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__=='__main__':
    main()
    