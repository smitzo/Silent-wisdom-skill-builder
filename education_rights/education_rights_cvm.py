import pygame
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
frame1 = os.getcwd()+"/assets/education_rights/EducationRights.png"
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

    l1 = Button(106,407,1746,90,white, '', white, '')
    l2 = Button(94,556,1746,90,white, '', white, '')
    l3 = Button(90,713,159,60,white, '', white, '')
    l4 = Button(90,821,635,57,white, '', white, '')
    l5 = Button(90,929,739,59,white, '', white, '')

    links = [l1,l2,l3,l4,l5]

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done = True
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if close_button.rect.collidepoint(event.pos):
                    done = True

                if l1.rect.collidepoint(event.pos):
                    webbrowser.open("https://ncert.nic.in/pdf/CWSN-FAQs.pdf")
                    done = True
                if l2.rect.collidepoint(event.pos):
                    webbrowser.open("https://www.livelaw.in/articles/rights-autistic-people-india-education-profession-medical-therapy-social-protection-231281")
                    done = True
                if l3.rect.collidepoint(event.pos):
                    webbrowser.open("https://dredf.org/legal-advocacy/international-disability-rights/international-laws/india-the-rights-of-persons-with-disabilities-act-2016/")
                    done = True
                if l4.rect.collidepoint(event.pos):
                    webbrowser.open("https://www.ijariit.com/manuscripts/v4i4/V4I4-1403.pdf")
                    done = True
                if l5.rect.collidepoint(event.pos):
                    webbrowser.open("https://vikaspedia.in/education/parents-corner/guidelines-for-parents-of-children-with-disabilities/legal-rights-of-the-disabled-in-india")
                    done = True

        screen.fill(white)
        screen.blit(image1,(0,0))
        close_button.draw(screen)  # Draw the close button
        pygame.display.flip()
        clock.tick()
        
    pygame.quit()

if __name__=='__main__':
    main()
