import pygame
#import pyttsx3
import webbrowser
import os
pygame.init()

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

#image
frame1 = os.getcwd()+ "/assets\employment_and_general_rights\EmploymentAndGeneralRights.png"
image1 = pygame.image.load(frame1)




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


# Print text in window
def print_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    # text_rect = text_surface.get_rect(center=(x,y))
    screen.blit(text_surface,(x,y))


def main():
    screen_info = pygame.display.Info()
    width, height = screen_info.current_w, screen_info.current_h

    # Close button properties (moved to top right)
    close_button = Button(1808, 30, 55, 55, 'red', 'X', white, 'close_button')


    # scholarship button
    s1_button = Button(75, 255, 821, 100, gray, "", 'red', 's1')
    s2_button = Button(75, 416, 821, 100, gray, "", 'red', 's1')
    s3_button = Button(75, 578, 821, 100, gray, "", 'red', 's1')
    s4_button = Button(75, 739, 821, 100, gray, " ", 'red', 's1')
    s5_button = Button(75, 900, 821, 100, gray, "", 'red', 's1')

    c1_button = Button(1029, 255, 821, 100, gray, "", 'red', 's1')
    c2_button = Button(1029, 416, 821, 100, gray, "", 'red', 's1')
    c3_button = Button(1029, 578, 821, 100, gray, "", 'red', 's1')
    c4_button = Button(1029, 739, 821, 100, gray, "", 'red', 's1')
    c5_button = Button(1029, 900, 821, 100, gray, "", 'red', 's1')

    scho_buttons = [s1_button,s2_button,s3_button,s4_button,s5_button]
    sche_buttons = [c1_button,c2_button,c3_button,c4_button,c5_button] 


    done = False
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done = True
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if close_button.rect.collidepoint(event.pos):
                    done = True

                    
                if s1_button.rect.collidepoint(event.pos):
                    webbrowser.open("https://enabled.in/wp/government-orders-for-persons-with-disabilities/")
                if s2_button.rect.collidepoint(event.pos):
                    webbrowser.open("https://cis-india.org/accessibility/blog/summary-of-judgments-on-disability-rights")
                if s3_button.rect.collidepoint(event.pos):
                    webbrowser.open("https://dredf.org/legal-advocacy/international-disability-rights/international-laws/india-the-rights-of-persons-with-disabilities-act-2016/")
                if s4_button.rect.collidepoint(event.pos):
                    webbrowser.open("https://pubmed.ncbi.nlm.nih.gov/27917445/")
                if s5_button.rect.collidepoint(event.pos):
                    webbrowser.open("http://www.ccdisabilities.nic.in/resources/om-notification")
                if c1_button.rect.collidepoint(event.pos):
                    webbrowser.open("https://vikaspedia.in/education/parents-corner/guidelines-for-parents-of-children-with-disabilities/legal-rights-of-the-disabled-in-india/")
                if c2_button.rect.collidepoint(event.pos):
                    webbrowser.open("https://enabled.in/wp/wp-content/uploads/2017/08/Reservation-for-Persons-with-Benchmark-Disabilities-Suggestions.pdf")
                if c3_button.rect.collidepoint(event.pos):
                    webbrowser.open("http://www.ccdisabilities.nic.in/resources/om-notification")
                if c4_button.rect.collidepoint(event.pos):
                    webbrowser.open("https://dredf.org/legal-advocacy/international-disability-rights/international-laws/india-the-rights-of-persons-with-disabilities-act-2016/")
                if c5_button.rect.collidepoint(event.pos):
                    webbrowser.open("https://www.myscheme.gov.in/schemes/mdiis")

                
        screen.fill(white)




        for button in scho_buttons:
            button.draw(screen)

        for button in sche_buttons:
            button.draw(screen)

        screen.blit(image1,(0,0))
        close_button.draw(screen)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__=='__main__':
    main()