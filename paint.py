import sys
import pygame
clock = pygame.time.Clock()
display_x =800
display_y=600
pygame.init()
window_surface = pygame.display.set_mode((display_x,800))

window_surface.fill((0,0,0))
grid_size_x=15
grid_size_y=15
x_box = [i for i in range(display_x//grid_size_x)]
y_box = [i for i in range(display_y//grid_size_y )]
def draw_grid():
    for i in range(display_x//grid_size_x):
        for j in range(display_y//grid_size_y):
            pygame.draw.rect(window_surface, (0, 0, 0), ((i*grid_size_x, j*grid_size_y),(grid_size_x, grid_size_y)),0)
            pygame.draw.rect(window_surface, (255, 255, 255), ((i*grid_size_x, j*grid_size_y),(grid_size_x, grid_size_y)), 2)
draw_grid()
color_pad =[(255,255,0),(97,251,255),(0,255,0),(255,0,0)]
color = 0
for i in range(2):
    for j in range(2):
        pygame.draw.rect(window_surface,color_pad[color],((100+i*30,620+j*30),(30,30)))
        color+=1
pygame.draw.rect(window_surface,(255,255,255),((500,620),(50,30)))
pygame.display.update()


        
def main():
    play = True
    color = 0
    while play:

    
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                play =False
            elif pygame.mouse.get_pressed()[0]:
                
                mouse_place = list(pygame.mouse.get_pos())
                if mouse_place[0] >=100 and mouse_place[0]< 130 and mouse_place[1]>620 and mouse_place[1]<650:
                    color =0
                    break
                elif mouse_place[0] >=100 and mouse_place[0]< 130 and mouse_place[1]>650 and mouse_place[1]<680:
                    color =1
                    break
                elif mouse_place[0] >=130 and mouse_place[0]< 160 and mouse_place[1]>620 and mouse_place[1]<650:
                    color =2
                    break
                elif mouse_place[0] >=130 and mouse_place[0]< 160 and mouse_place[1]>650 and mouse_place[1]<680:
                    color =3
                    break
                elif mouse_place[0] >=500 and mouse_place[0]<550 and mouse_place[1]>620 and mouse_place[1]<650:
                    draw_grid()
                    break
                mouse_place[0] = mouse_place[0]//grid_size_x
                mouse_place[1] = mouse_place[1]//grid_size_y

                while mouse_place[0] not in x_box:
                    mouse_place[0]-=1
                while mouse_place[1] not in y_box:
                    mouse_place[1]-=1
                
                pygame.draw.rect(window_surface,color_pad[color], ((mouse_place[0]*grid_size_x,mouse_place[1]*grid_size_y),(grid_size_x, grid_size_y)), 0)
            elif pygame.mouse.get_pressed()[2]:
                
                mouse_place = list(pygame.mouse.get_pos())
                mouse_place[0] = mouse_place[0]//grid_size_x
                mouse_place[1] = mouse_place[1]//grid_size_y
                
                while mouse_place[0] not in x_box:
                    mouse_place[0]-=1
                while mouse_place[1] not in y_box:
                    mouse_place[1]-=1
                
                pygame.draw.rect(window_surface, (0, 0, 0), ((mouse_place[0]*grid_size_x,mouse_place[1]*grid_size_y),(grid_size_x, grid_size_y)),0)
                pygame.draw.rect(window_surface, (255, 255, 255), ((mouse_place[0]*grid_size_x,mouse_place[1]*grid_size_y),(grid_size_x, grid_size_y)),2)
            
            
            pygame.display.update()



if __name__ == "__main__":
    main()