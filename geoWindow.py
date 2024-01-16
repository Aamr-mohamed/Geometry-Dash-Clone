import pygame

window=pygame.display.set_mode((500,500))

pygame.display.set_caption("geometry Dash babeee!!")

x,y=50,400
width,height=40,50
vel=5

run=True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        y-=vel


    window.fill((0,0,0))
    pygame.draw.rect(window,(255,0,0),(x,y,width,height))
    pygame.display.update()


pygame.quit()
