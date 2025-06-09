import os
import pgzrun 
import random

os.environ['SDL_VIDEO_CENTERED'] = '1'

#constante 
WIDTH = 800
HEIGHT = 449 

LEFT_LIMIT = 60
RIGHT_LIMIT = WIDTH - 60
X_MIN = 20
X_MAX = WIDTH - 20

#variavel
playlist = ['life_in_the_world','the_woodwind_song','life_in_the_world','the_woodwind_song']
score = 0
life = 5
start = False
game_over = False
end_points = 0 
sound_on = True

#fundo
bg = Actor('background')

#barco
ship = Actor('ship')
ship.x = 400
ship.y = 360 

#moeda
coin = Actor('coin')
coin.pos = (random.randint(X_MIN, X_MAX), 0)

#caveira
skull = Actor('skull')
skull.pos = (random.randint(X_MIN, X_MAX), 0)

#bomba
bomb = Actor('bomb2')
bomb.pos = (random.randint(X_MIN, X_MAX), 0)

def reset_game():
    global score, life, end_points, game_over, start, playlist
    
    score = 0
    life = 5
    end_points = 0
    game_over = False
    start = True
    
    coin.pos = (random.randint(X_MIN, X_MAX), 0)
    skull.pos = (random.randint(X_MIN, X_MAX), 0)
    bomb.pos = (random.randint(X_MIN, X_MAX), 0)
    ship.pos = (400, 360)
    
    if sound_on:
        music.play_once(playlist[0])
        music.queue(playlist[1]) 
        music.queue(playlist[2]) 
        music.queue(playlist[3]) 

#funcao de movimento e inverção do barco
def move_ship():
    #movimenta o barco para a esquerda e direita 
    if keyboard.left:
        ship.image = 'ship'
        ship.x -= 5
    
    if keyboard.right:
        ship.image = 'ship_inverted' 
        ship.x += 5

#limitando movimento do barco no eixo x
    if ship.x < LEFT_LIMIT:
        ship.x = LEFT_LIMIT
    if ship.x > RIGHT_LIMIT:
        ship.x = RIGHT_LIMIT

def reset_object(): 
    global score, life, game_over, end_points, sound_on, start
    #reiniciando os objetos
    coin.y += 3 
    if coin.y > HEIGHT:
        coin.pos = (random.randint(X_MIN, X_MAX), 0)
    
    if coin.colliderect(ship):
        if sound_on:
            sounds.coin_up2.play()
        

        coin.pos = (random.randint(X_MIN, X_MAX), 0)
        score += 1
        end_points += 1 
        
        if score == 10:
            if sound_on:
                sounds.life_up.play()
            
            score = 0
            life += 1
        
    skull.y += 2
    if skull.y > HEIGHT:  
        skull.pos = (random.randint(X_MIN, X_MAX), 0)

    if skull.colliderect(ship):
        if sound_on:
            sounds.skull_bone.play()

        skull.pos = (random.randint(X_MIN, X_MAX), 0)
        
        if life > 0:
            if sound_on:
                sounds.life_down.play()
        
            life -= 1
       
        elif life == 0:
            game_over = True
       
    bomb.y += 4
    if bomb.y > HEIGHT:
        bomb.pos = (random.randint(X_MIN, X_MAX), 0)
    
    if bomb.colliderect(ship):
        if sound_on:
            sounds.bomb_explosion.play()
        
        bomb.pos = (random.randint(X_MIN, X_MAX), 0)
           
        if score > 0:
            score -= 1
        
        elif life > 0:
            
            if sound_on:
                sounds.life_down.play()
           
            life -= 1
            score = 9
        
        if life == 0 and score == 0:
            game_over = True
             
def draw():
    bg.draw()
    draw_menu()
    if game_over == True:
        screen.draw.text('GAME OVER', center = (WIDTH // 2, HEIGHT // 2 - 30), color = (255,255,255), fontsize = 30)
        screen.draw.text('FINAL SCORE: ' + str(end_points), center=(WIDTH // 2, HEIGHT // 2 + 20), color = (255,255,255), fontsize = 30)
    
    elif start == True:
        screen.draw.text('Score: ' + str(score), (10, 50), color = (255,255,255), fontsize = 30)
        screen.draw.text('Life: ' + str(life), (730, 50), color = (255,255,255), fontsize = 30)
        ship.draw()
        coin.draw()
        skull.draw()
        bomb.draw()
    
       
        
# Definindo os botões do menu
menu_buttons = [
    {"label": "COMEÇAR", "rect": Rect((0, 0), (266, 40))},
    {"label": "SOM : ON / SOM : OFF", "rect": Rect((266, 0), (266, 40))},
    {"label": "SAIR", "rect": Rect((533, 0), (266, 40))}
]

# Desenhar a barra de menu
def draw_menu():
    for button in menu_buttons:
        screen.draw.filled_rect(button["rect"], "black")
        screen.draw.rect(button["rect"], "white")
        screen.draw.text(
            button["label"],
            center=button["rect"].center,
            color="white",
            fontsize=30
        )

# Evento de clique do mouse
def on_mouse_down(pos):
    for button in menu_buttons:
        
        if button["rect"].collidepoint(pos):
            handle_menu_action(button["label"])

# Tratamento das ações dos botões
def handle_menu_action(label):
    global sound_on, start
    if label == "COMEÇAR":
        reset_game() 
               

    elif label == "SOM : ON / SOM : OFF":
        sound_on = not sound_on
        if sound_on:
            music.set_volume(1)

        else:
            music.set_volume(0)
            
    elif label == "SAIR":
        exit()  # Fecha o jogo

    
def update():
           
    if start == True and game_over == False:
        move_ship()
        reset_object()
       
pgzrun.go()
