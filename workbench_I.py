import pygame, sys, moviepy.editor
 
# Inicializar Pygame ------------------------------------------------------------------------------------
pygame.init()

# Crear la pantalla ------------------------------------------------------------------------------------
pantalla = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

# imagenes ------------------------------------------------------------------------------------
marco = pygame.transform.scale(pygame.image.load("img/backgrounds/marco-seleccion.png"), (260, 265))
BG = pygame.image.load("img/backgrounds/BACKGROUND.png")
BG_MENU = pygame.image.load("img/backgrounds/Menu_I_Was_Here.png")
BG_CSJ = pygame.image.load("img/backgrounds/BG_CSJ.png")
# FINALES
F1 = pygame.image.load("img/finales/F1.jpg")
F2 = pygame.image.load("img/finales/F2.jpg")
F3 = pygame.image.load("img/finales/F3.jpg")
F4 = pygame.image.load("img/finales/F4.jpg")
F5 = pygame.image.load("img/finales/F5.jpg")
F6 = pygame.image.load("img/finales/F6.jpg")
F7 = pygame.image.load("img/finales/F7.jpg")
F8 = pygame.image.load("img/finales/F8.png")
# Colores ------------------------------------------------------------------------------------
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
C_Energia = (255, 227, 66)
C_Sum_vida = (84, 196, 94)
C_Reputacion = (254, 112, 122)
C_Tecnologia = (109, 177, 255)

# Fuente ---------------------------------------------------------------------------------------------
fuente_r = pygame.font.Font("fuentes/gamefont.otf", 46)
fuente_p = pygame.font.Font("fuentes/gamefont.otf", 70)

# Musica ---------------------------------------------------------------------------------------------
FX_R = pygame.mixer.Sound("sound/FX/select_R.mp3")
FX_L = pygame.mixer.Sound("sound/FX/select_L.mp3")

# saltos de linea ------------------------------------------------------------------------------------

def renderizar_texto_con_saltos(texto, posicion):
    lineas = texto.split('\n')  # Divide el texto en líneas en cada salto de línea
    y = posicion[1]  # Posición vertical inicial
    for linea in lineas:
        texto_renderizado = fuente_p.render(linea, True, NEGRO)  # Renderiza la línea
        pantalla.blit(texto_renderizado, (posicion[0], y))  # Dibuja la línea
        y += texto_renderizado.get_height() # Incrementa la posición vertical para la siguiente línea
        
def renderizar_texto_con_saltos_r(texto, posicion):
    lineas = texto.split('\n')  # Divide el texto en líneas en cada salto de línea
    y = posicion[1]  # Posición vertical inicial
    for linea in lineas:
        texto_renderizado = fuente_r.render(linea, True, NEGRO)  # Renderiza la línea
        pantalla.blit(texto_renderizado, (posicion[0], y))  # Dibuja la línea
        y += texto_renderizado.get_height() # Incrementa la posición vertical para la siguiente línea
        
def main_menu():
    pygame.display.set_caption("Menu")
    
    pixel_p_continuar_menu_x = 630
    pixel_p_continuar_menu_y = 550
    
    text_p_continuar_pos = (pixel_p_continuar_menu_x, pixel_p_continuar_menu_y)
    opacity = 255
    
    pixel_csj_menu_x = 260
    pixel_csj_menu_y = 50
    
    text_csj_pos = (pixel_csj_menu_x, pixel_csj_menu_y)
    
    # música de fondo
    ruta_musica = "sound/songs/bgm_menu.mp3"
    musica_fondo = pygame.mixer.music.load(ruta_musica)
    pygame.mixer.music.play(-1)
    
    
    while True:
        pantalla.blit(BG_MENU, (0, 0))
        
        text_p_continuar = fuente_p.render("Presiona espacio para continuar", True, ROJO)
        text_p_continuar.set_alpha(opacity)
        text_p_continuar_rect = text_p_continuar.get_rect(center=text_p_continuar_pos)
        
        pantalla.blit(text_p_continuar, text_p_continuar_rect)
        
        text_csj = fuente_p.render("Presiona Q para ver cómo se juega", True, (254, 110, 100))
        text_csj_rect = text_csj.get_rect(center=text_csj_pos)
        
        pantalla.blit(text_csj, text_csj_rect)
        
        opacity -= 1.7
        if opacity <= 0:
            opacity = 255
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ruta_musica1 = "sound/songs/bgm.mp3"
                    pygame.mixer.music.load(ruta_musica1)
                    pygame.mixer.music.play(-1)
                    play()
                elif event.key == pygame.K_q:
                    como_se_juega()
                elif event.key == pygame.K_b:
                    creditos()

        pygame.display.update()
        
def como_se_juega():
    pygame.display.set_caption("Como se juega")

    # música de fondo
    
    
    pixel_p_continuar_x = 630
    pixel_p_continuar_y = 620
    text_pos_p_continuar = (pixel_p_continuar_x, pixel_p_continuar_y)
    opacity = 255
    
    pixel_csj_zona_x = 170
    pixel_csj_zona_y = 680
    text_pos_csj_zona = (pixel_csj_zona_x, pixel_csj_zona_y)
    
    pixel_csj_menu_x = 650
    pixel_csj_menu_y = 690
    text_pos_csj_menu = (pixel_csj_menu_x, pixel_csj_menu_y)
    

    while True:
        pantalla.blit(BG_CSJ, (0, 0))
        
        text_p_continuar = fuente_p.render("Presiona espacio para continuar", True, ROJO)
        text_p_continuar.set_alpha(opacity)
        text_rect_p_continuar = text_p_continuar.get_rect(center=text_pos_p_continuar)
        
        pantalla.blit(text_p_continuar, text_rect_p_continuar)
        
        text_csj_zona = fuente_p.render("Zona", True, NEGRO)
        text_rect_csj_zona = text_csj_zona.get_rect(center=text_pos_csj_zona)
        
        pantalla.blit(text_csj_zona, text_rect_csj_zona)
        
        text_csj_menu = fuente_p.render("ESC para volver al menu", True, BLANCO)
        text_rect_csj_menu = text_csj_menu.get_rect(center=text_pos_csj_menu)
        
        pantalla.blit(text_csj_menu, text_rect_csj_menu)
        
        opacity -= 1.7
        if opacity <= 0:
            opacity = 255

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ruta_musica1 = "sound/songs/bgm.mp3"
                    musica_fondo = pygame.mixer.music.load(ruta_musica1)
                    pygame.mixer.music.play(-1)
                    play()
                if event.key == pygame.K_ESCAPE:
                    main_menu()

        pygame.display.update()

   
def play():
    pygame.display.set_caption("Juego")
    
    # estadisticas juego -------------------------------------------------------------------------------------------
    energia = 6
    suministros_de_vida = 6
    reputacion = 6
    tecnologia = 6
    
    #NPCS+QUE ES
    gustabojpg = pygame.image.load("img/npcs/gustabo.jpg")
    gustabojpg = pygame.transform.scale(gustabojpg, (520, 324))
    gustabopng = pygame.image.load("img/npcs/gustabo.png")
    gustabopng = pygame.transform.scale(gustabopng, (480, 480))
    alfredojpg = pygame.image.load("img/npcs/alfredo.jpg")
    alfredojpg = pygame.transform.scale(alfredojpg, (520, 324))
    alfredopng = pygame.image.load("img/npcs/alfredo.png")
    alfredopng = pygame.transform.scale(alfredopng, (480, 480))
    alienjpg = pygame.image.load("img/npcs/alien.jpg")
    alienjpg = pygame.transform.scale(alienjpg, (520, 324))
    alienpng = pygame.image.load("img/npcs/alien.png")
    alienpng = pygame.transform.scale(alienpng, (480, 480))
    cabrajpg = pygame.image.load("img/npcs/cabra.jpg")
    cabrajpg = pygame.transform.scale(cabrajpg, (520, 324))
    cabrapng = pygame.image.load("img/npcs/cabra.png")
    cabrapng = pygame.transform.scale(cabrapng, (480, 480))
    lobojpg = pygame.image.load("img/npcs/lobo.jpg")
    lobojpg = pygame.transform.scale(lobojpg, (520, 324))
    lobopng = pygame.image.load("img/npcs/lobo.png")
    lobopng = pygame.transform.scale(lobopng, (480, 480))
    desc_gustabo = fuente_p.render("Tripulante de la Nave", 3, AMARILLO)
    desc_alfredo = fuente_p.render("IA de la nave", 3, AMARILLO)
    desc_alien = fuente_p.render("E", 3, AMARILLO)
    desc_cabra = fuente_p.render("Vendedor Ambulante", 3, AMARILLO)
    desc_lobo = fuente_p.render("Guerrero ", 3, AMARILLO)
    
    
#  variables respuestas y preguntas ------------------------------------------------------------------------------  
    p1 = "Toda la nave acaba de despertar de "
    p1_1 = "una criogenización. ¿Qué quieres"
    p1_2 = "hacer, Comandante?"
    r1 = "Organizar reunión"
    r2 = "Saludar a toda "
    r2_1 = "la tripulación"
    p2 = "¿Sobre qué irá la reunión?"
    r3 = "Revisar protocolos"
    r4 = "Conocer tripulación"

    p3 = "¿Qué es más conveniente, presentar "
    p3_1 = "a la tripulación o hacer un discurso?"
    r5 = "Presentación"
    r6 = "Discurso breve"

    p4 = "¿Qué protocolos deseas revisar?"
    r7 = "Revisar procedimien-"
    r7_1 = "tos de emergencia"
    r8 = "Revisar seguridad"

    p5 = "¿Cómo deseas conocer a la tripulación?"
    r9 = "Presentarse uno "
    r9_1= "por uno"
    r10 = "Presentación grupal"

    p6 = "¿Cómo quieres presentar a la tripulación?"
    r11 = "Individual"
    r12 = "En grupo"

    p7 = "¿Cuál va a ser el tema del discurso?"
    r13 = "Hablar sobre el "
    r13_1 = "objetivo de la misión"
    r14 = "Hablar sobre los "
    r14_1 = "logros de la tripulación"

    p8 = "Todo parece estar correcto, recuerda "
    p8_1 = "volver a revisar los protocolos"
    rempty = ""

    p9 = "Tienes dos mensajes, una señal de S.O.S "
    p9_1 = "en el planeta Nébula o ir al Mercado de "
    p9_2 = "la galaxia Andromeda Celestial"
    r15 = "Dirigirse al "
    r15_1 = "Mercado Celestial"
    r16 = "Ir hacia la "
    r16_1 = "señal S.O.S"

    p10 = "Llegas al mercado y el camino se bifurca "
    p10_1 = "en dos, camino izq. lleno de colores y"
    p10_2 = "tiendas, a diferencia del der. que"
    p10_3 = "es oscuro."
    r17 = "izquierda"
    r18 = "derecha"

    p11 = "La señal está a 400 años luz, llegas a la "
    p11_1 = "órbita del planeta antes de aterrizar"
    p11_2 = "¿qué quieres hacer?"
    r19 = "Revisar suministros "
    r19_1 = "y equipo"
    r20 = "Establecer punto "
    r20_1 = "de aterrizaje"

    p12 = "Entre todos los puestos se puede"
    p12_1 = "observar a un ser desconocido"
    p12_2 = "robando a otro"
    r21 = "Ayudar"
    r22 = "No hacer caso y "
    r22_1 = "seguir caminando"

    p13 = "Se puede apreciar una figura oscura"
    p13_1 = "de aspecto humanoide en una tienda"
    p13_2 = "poco iluminada"
    r23 = "Volver al camino"
    r23_1 = "con tiendas"
    r24 = "Acercarse a la "
    r24_1 = "figura misteriosa"

    p14 = "Parece que el nivel de los tanques de "
    p14_1 = "oxígeno está bajando a un ritmo irregular,"
    p14_2 = "tenlo en cuenta..."
    r25 = "Muy arriesgado,"
    r25_1 = " vuelvo al mercado"
    r26 = "Continuar sin "
    r26_1 = "miedo a nada"
    F6 = "Has muerto por pérdida de O2"

    p15 = "Ten en cuenta que la señal no es exacta,"
    p15_1 = "¿quieres aterrizar en el sur del planeta"
    p15_2 = "o en el norte?"
    r27 = "Sur"
    r28 = "Norte"
    F7 = "Se han perdido las coordenadas"

    p16 = "Empiezas a correr y te das cuenta de"
    p16_1 = "que es más rápido que tú y lo estás"
    p16_2 = "perdiendo de vista poco a poco, ¿qué "
    p16_3 = "vas a hacer?"
    r29 = "Seguir corriendo, no"
    r29_1 = "ha podido irse muy"
    r29_2 = "lejos"
    r30 = "Darte por vencido y"
    r30_1= "volver al mercado"

    p17 = "El traficante te ofrece tecnología a"
    p17_1 = "cambio de suministros de vida."
    r31 = "Rechazar el inter-"
    r31_1 = "cambio y volver"
    r32 = "Aceptar el "
    r32_1 = "intercambio"

    p18 = "Durante la persecución, el camino se"
    p18_1 = "bifurca en dos, ¿por qué camino irás?"
    r33 = "Izquierda"
    r34 = "Derecha"

    p19 = "Una vez dentro del bar, a lo lejos"
    p19_1 = "escuchas a alguien hablando de un "
    p19_2 = "gremio llamado Guardia Celestial, esto "
    p19_3 = "llama tu atención y decides ir. "

    p20 = "Continúas caminando y entras a un bar"
    p20_1 = "local, a lo lejos escuchas a alguien "
    p20_2 = "hablando de un gremio llamado Guardia"
    p20_3 = "Celestial esto te tenta y decides ir."

    p21 = "Al volver, entras a un bar local a tomar "
    p21_1 = "algo, a lo lejos escuchas a alguien "
    p21_2 = "hablando de un gremio llamado Guardia"
    p21_3 = "Celestial, llama tu atención y decides ir."

    p22 = "Dentro ves a mucha gente reunida en un"
    p22_1= "marco de madera, decides preguntar a un"
    p22_2 = "ser local sobre ello, este te comenta que "
    p22_2_1 = "es un tablero de encargos,"
    
    p22_3 = "para poder hacer uso de el tienes que"
    p22_4 = "registrar tu nave y tripulación en "
    p22_5 = "el gremio Guardia Celestial."
    r39 = "Registrarse en "
    r39_1 = "el gremio"

    p23 = "Te has adentrado en un callejón sin "
    p23_1 = "salida y has perdido al ladrón"
    r35 = "Seguir buscando"
    r36 = "Darte por vencido y "
    r36_1 = "volver con la "
    r36_2 = "tripulación"

    p24 = "Te has adentrado en un callejón sin "
    p24_1 = "salida y has arrinconado al ladrón,"
    p24_2 = " ¿qué vas a hacer?"
    r37 = "Darle una paliza y "
    r37_1 = "quedarte con los "
    r37_2 = "objetos robados"
    r38 = "Recuperar lo robado "
    r38_1 = "y dejarlo ir"

    p25 = "Después de una prolongada búsqueda "
    p25_1 = "no encuentras al ladrón y te das "
    p25_2 = "por vencido, al volver, parte de "
    p25_3 = "la tripulación te mira con orgullo"

    p26 = "Al volver sin nada después de darte "
    p26_1 = "por vencido en la persecución, parte "
    p26_2 = "de la tripulación te mira con orgullo"

    p27 = "Al volver con la tripulación,"
    p27_1 = "estos te miran con desprecio"

    p28 = "Después de devolver lo robado a "
    p28_1 = "su propietario, tu tripulación te "
    p28_2 = "mira con orgullo te mira con orgullo"

    p29 = "Una vez reunido con la tripulación"
    p29_1 = "¿qué decides hacer?"
    r40 = "Volver a la nave y"
    r40_1 = "explorar la Galaxia"
    r40_2 = "Andromeda"
    F1 = "No puedes volver..."
    r41 = "Ir a un bar local,"
    r41_1 = "quien sabe lo que"
    r41_2 = "puedes encontrar"

    p30 = "Una vez registrado en el gremio, decides"
    p30_1 = "mirar el tablón de encargos."
    p30_2 = "¿Qué encargo vas a aceptar?"
    r42 = "Reconquistar planeta "
    r42_1 = "LT-782 habitado por  "
    r42_2 = "Autómatas a 5 años luz"
    r43 = "Eliminar Terminoides"
    r43_1 = "y recuperar los"
    r43_2 = " datos en LV-532,"
    r43_3 = "a 20 años luz"


    p32 = "Te estás aproximando a la órbita del "
    p32_1 = "planeta LT-782, ¿dónde deseas "
    p32_2 = "aterrizar?"
    r44 = "Sur"
    r45 = "Norte"
    F2 = "Un antiaéreo ha destruido la nave, "
    F2_1 = "nadie ha sobrevivido"

    p33 = "Te estás aproximando a la órbita del "
    p33_1 = "planeta LV-532, ¿dónde deseas "
    p33_2 = "aterrizar?"
    r46 = "Sur"
    r47 = "Norte"

    p34 = "Al aterrizar, se puede observar a "
    p34_1 = "lo lejos un enjambre de Terminoides"
    F3 = "Los enfrentas con todo el equipo pero te exterminan"

    p35 = "Al aterrizar, se puede observar un "
    p35_1 = "puesto de investigación en ruinas,"
    p35_2 = "¿qué deseas hacer?"
    r48 = "Asegurar la zona de "
    r48_1 = "aterrizaje"
    F4 = "Del puesto de investigación emergen"
    F4_1 = "Terminoides y te aniquilan"
    r49 = "Dirigirte a la zona "
    r49_1 = "en ruinas"
    F5 = "Encuentras una horda de Terminoides"
    F5_1 = "y te acorralan"

    F8 = "Te has quedado sin recursos, has muerto"
    
    #Zonas-----------------------------------------------------------------------------------------------------------------
    Z1 = "Sombra Estelar (nave)"
    Z2 = "Sala de Reuniones"
    Z3 = "Zona generadores"
    Z4 = "Habitaciones"
    Z5 = "Zona de mandos"
    Z6 = "Mercado Celestial"
    Z7 = "Camino oscuro"
    Z8 = "Callejón"
    Z9 = "Bar"
    Z10 = "Planeta LT-782"
    Z11 = "Planeta LV-532"
    Z12 = "¿Cielo o infierno?"

    indice_pregunta = 1
        
    while True: # Manejo de eventos
             
         
            pantalla.blit(BG, (0, 0))
            
            texto_reputacion = fuente_p.render("Reputación: " + str(reputacion), True, C_Reputacion)
            texto_sum_vida = fuente_p.render("Suministros de vida: " + str(suministros_de_vida), True, C_Sum_vida)
            texto_tecnologia = fuente_p.render("Tecnología: " + str(tecnologia), True, C_Tecnologia)
            texto_Rec_energetico = fuente_p.render("Recurso energético: " + str(energia), True, C_Energia)
            
            pantalla.blit(texto_reputacion, (20, 20))
            pantalla.blit(texto_tecnologia, (20, 60))
            pantalla.blit(texto_sum_vida, (20, 100))
            pantalla.blit(texto_Rec_energetico, (20, 140))

            if energia <= 0 or suministros_de_vida <= 0 or reputacion <= 0 or tecnologia <= 0: # Si las estadisiticas llegan a 0 el juego muestra en pantalla la variable F8, tiene q actualizar la pantalla para mostrartelo y como se supone que has muerto tienes que poner un while true para finazliar el juego sino el juego sigue funcionando.
                f8()
                
# Renderizar la pregunta actual ------------------------------------------------------------------------------------
            
#segunda linea pregunta renderizar_texto_con_saltos(p, (400, 185)) || si estas apurado coge esta renderizar_texto_con_saltos(p, (385, 185))
#tercera linea pregunta renderizar_texto_con_saltos(p, (400, 220)) || si estas apurado coge esta renderizar_texto_con_saltos(p, (385, 220))
# quarta linea en caso extremo renderizar_texto_con_saltos(p, (400, 255)) || si estas apurado coge esta renderizar_texto_con_saltos(p, (385, 255))
                       
# Renderizar las respuestas ------------------poner # // si funci------------------------------------------------------------------
#coordenadas respuesta izq: renderizar_texto_con_saltos_r(r, (430, 450)) || renderizar_texto_con_saltos_r(r, (430, 475))
# coordenadas respuesta der: renderizar_texto_con_saltos_r(r, (695, 450)) ||renderizar_texto_con_saltos_r(r, (695, 475))            
# Actualizar la pantalla ------------------------------------------------------------------------------------
            else :
                if indice_pregunta == 1:
                    texto_pregunta = fuente_p.render(p1, True, NEGRO)
                    renderizar_texto_con_saltos(p1_1, (400, 185))
                    renderizar_texto_con_saltos(p1_2, (400, 220))
                    respuestaizq = fuente_r.render(r1, True, NEGRO)
                    respuestader = fuente_r.render(r2, True, NEGRO)
                    renderizar_texto_con_saltos_r(r2_1, (695, 450))
                    texto_zona = fuente_p.render(Z1, True, BLANCO)
                elif indice_pregunta == 2:
                    texto_pregunta = fuente_p.render(p2, True, NEGRO)
                    respuestaizq = fuente_r.render(r3, True, NEGRO)
                    respuestader = fuente_r.render(r4, True, NEGRO)
                    texto_zona = fuente_p.render(Z2, True, BLANCO)
                elif indice_pregunta == 3:
                    texto_pregunta = fuente_p.render(p3, True, NEGRO)
                    renderizar_texto_con_saltos(p3_1, (400, 185))
                    respuestaizq = fuente_r.render(r5, True, NEGRO)
                    respuestader = fuente_r.render(r6, True, NEGRO)
                    texto_zona = fuente_p.render(Z2, True, BLANCO)
                elif indice_pregunta == 4:
                    texto_pregunta = fuente_p.render(p4, True, NEGRO)
                    respuestaizq = fuente_r.render(r7, True, NEGRO)
                    renderizar_texto_con_saltos_r(r7_1, (430, 450))
                    respuestader = fuente_r.render(r8, True, NEGRO)
                    texto_zona = fuente_p.render(Z3, True, BLANCO)
                elif indice_pregunta == 5:
                    texto_pregunta = fuente_p.render(p5, True, NEGRO)
                    respuestaizq = fuente_r.render(r9, True, NEGRO)
                    renderizar_texto_con_saltos_r(r9_1, (430, 450))
                    respuestader = fuente_r.render(r10, True, NEGRO)
                    texto_zona = fuente_p.render(Z2, True, BLANCO)
                elif indice_pregunta == 6:
                    texto_pregunta = fuente_p.render(p6, True, NEGRO)
                    respuestaizq = fuente_r.render(r11, True, NEGRO)
                    respuestader = fuente_r.render(r12, True, NEGRO)
                    texto_zona = fuente_p.render(Z4, True, BLANCO)
                elif indice_pregunta == 7:
                    texto_pregunta = fuente_p.render(p7, True, NEGRO)
                    respuestaizq = fuente_r.render(r13, True, NEGRO)
                    renderizar_texto_con_saltos_r(r13_1, (430, 450))
                    respuestader = fuente_r.render(r14, True, NEGRO)
                    renderizar_texto_con_saltos_r(r14_1, (685, 450))
                    texto_zona = fuente_p.render(Z2, True, BLANCO)
                elif indice_pregunta == 8:
                    texto_pregunta = fuente_p.render(p8, True, NEGRO)
                    renderizar_texto_con_saltos(p8_1, (400, 185))
                    respuestaizq = fuente_r.render(rempty, True, NEGRO)
                    respuestader = fuente_r.render(rempty, True, NEGRO)
                    pantalla.blit(alfredojpg, (380, 331))
                    pantalla.blit(desc_alfredo, (560, 665))
                    texto_zona = fuente_p.render(Z3, True, BLANCO)
                elif indice_pregunta == 9:
                    texto_pregunta = fuente_p.render(p9, True, NEGRO)
                    renderizar_texto_con_saltos(p9_1, (385, 185))
                    renderizar_texto_con_saltos(p9_2, (385, 220))
                    respuestaizq = fuente_r.render(r15, True, NEGRO)
                    renderizar_texto_con_saltos_r(r15_1, (430, 450))
                    respuestader = fuente_r.render(r16, True, NEGRO)
                    renderizar_texto_con_saltos_r(r16_1, (695, 450))  
                    texto_zona = fuente_p.render(Z5, True, BLANCO) 
                elif indice_pregunta == 10:
                    texto_pregunta = fuente_p.render(p10, True, NEGRO)
                    renderizar_texto_con_saltos(p10_1, (385, 185))
                    renderizar_texto_con_saltos(p10_2, (385, 220))
                    renderizar_texto_con_saltos(p10_3, (385, 255))
                    respuestaizq = fuente_r.render(r17, True, NEGRO)
                    respuestader = fuente_r.render(r18, True, NEGRO)
                    texto_zona = fuente_p.render(Z6, True, BLANCO)
                elif indice_pregunta == 11:
                    texto_pregunta = fuente_p.render(p11, True, NEGRO)
                    renderizar_texto_con_saltos(p11_1, (400, 185))
                    renderizar_texto_con_saltos(p11_2, (400, 220))
                    respuestaizq = fuente_r.render(r19, True, NEGRO)
                    renderizar_texto_con_saltos_r(r19_1, (430, 450))
                    respuestader = fuente_r.render(r20, True, NEGRO)
                    renderizar_texto_con_saltos_r(r20_1, (695, 450))
                    texto_zona = fuente_p.render(Z5, True, BLANCO)
                elif indice_pregunta == 12:
                    texto_pregunta = fuente_p.render(p12, True, NEGRO)
                    renderizar_texto_con_saltos(p12_1, (400, 185))
                    renderizar_texto_con_saltos(p12_2, (400, 220))
                    respuestaizq = fuente_r.render(r21, True, NEGRO)
                    respuestader = fuente_r.render(r22, True, NEGRO)
                    renderizar_texto_con_saltos_r(r22_1, (695, 450))
                    texto_zona = fuente_p.render(Z6, True, BLANCO)
                    pantalla.blit(lobopng, (795, 255))
                    pantalla.blit(desc_lobo, (520, 665))
                elif indice_pregunta == 13:
                    texto_pregunta = fuente_p.render(p13, True, NEGRO)
                    renderizar_texto_con_saltos(p13_1, (400, 185))
                    renderizar_texto_con_saltos(p13_2, (400, 220))
                    respuestaizq = fuente_r.render(r23, True, NEGRO)
                    renderizar_texto_con_saltos_r(r23_1, (430, 450))
                    respuestader = fuente_r.render(r24, True, NEGRO)
                    renderizar_texto_con_saltos_r(r24_1, (685, 450))
                    texto_zona = fuente_p.render(Z7, True, BLANCO)
                elif indice_pregunta == 14:
                    texto_pregunta = fuente_p.render(p14, True, NEGRO)
                    renderizar_texto_con_saltos(p14_1, (385, 185))
                    renderizar_texto_con_saltos(p14_2, (385, 220))
                    respuestaizq = fuente_r.render(r25, True, NEGRO)
                    renderizar_texto_con_saltos_r(r25_1, (430, 450))
                    respuestader = fuente_r.render(r26, True, NEGRO)
                    renderizar_texto_con_saltos_r(r26_1, (695, 450))
                    texto_zona = fuente_p.render(Z3, True, BLANCO)
                elif indice_pregunta == 15:
                    texto_pregunta = fuente_p.render(p15, True, NEGRO)
                    renderizar_texto_con_saltos(p15_1, (400, 185))
                    renderizar_texto_con_saltos(p15_2, (400, 220))
                    respuestaizq = fuente_r.render(r27, True, NEGRO)
                    respuestader = fuente_r.render(r28, True, NEGRO)
                    texto_zona = fuente_p.render(Z5, True, BLANCO)
                elif indice_pregunta == 16:
                    texto_pregunta = fuente_p.render(p16, True, NEGRO)
                    renderizar_texto_con_saltos(p16_1, (400, 185))
                    renderizar_texto_con_saltos(p16_2, (400, 220))
                    renderizar_texto_con_saltos(p16_3, (400, 255))
                    respuestaizq = fuente_r.render(r29, True, NEGRO)
                    renderizar_texto_con_saltos_r(r29_1, (430, 450))
                    renderizar_texto_con_saltos_r(r29_2, (430, 475))
                    respuestader = fuente_r.render(r30, True, NEGRO)
                    renderizar_texto_con_saltos_r(r30_1, (695, 450))
                    texto_zona = fuente_p.render(Z8, True, BLANCO)
                elif indice_pregunta == 17:
                    texto_pregunta = fuente_p.render(p17, True, NEGRO)
                    renderizar_texto_con_saltos(p17_1, (400, 185))
                    respuestaizq = fuente_r.render(r31, True, NEGRO)
                    renderizar_texto_con_saltos_r(r31_1, (430, 450))
                    respuestader = fuente_r.render(r32, True, NEGRO)
                    renderizar_texto_con_saltos_r(r32_1, (695, 450))
                    texto_zona = fuente_p.render(Z7, True, BLANCO)
                    pantalla.blit(cabrapng, (795, 255))
                    pantalla.blit(desc_cabra, (520, 665))
                elif indice_pregunta == 18:
                    texto_pregunta = fuente_p.render(p18, True, NEGRO)
                    renderizar_texto_con_saltos(p18_1, (400, 185))
                    respuestaizq = fuente_r.render(r33, True, NEGRO)
                    respuestader = fuente_r.render(r34, True, NEGRO)
                    texto_zona = fuente_p.render(Z8, True, BLANCO)
                elif indice_pregunta == 19:
                    texto_pregunta = fuente_p.render(p19, True, NEGRO)
                    renderizar_texto_con_saltos(p19_1, (400, 185))
                    renderizar_texto_con_saltos(p19_2, (400, 220))
                    renderizar_texto_con_saltos(p19_3, (400, 255))
                    respuestaizq = fuente_r.render(rempty, True, NEGRO)
                    respuestader = fuente_r.render(rempty, True, NEGRO)
                    texto_zona = fuente_p.render(Z9, True, BLANCO)
                elif indice_pregunta == 20:
                    texto_pregunta = fuente_p.render(p20, True, NEGRO)
                    renderizar_texto_con_saltos(p20_1, (400, 185))
                    renderizar_texto_con_saltos(p20_2, (400, 220))
                    renderizar_texto_con_saltos(p20_3, (400, 255))
                    respuestaizq = fuente_r.render(rempty, True, NEGRO)
                    respuestader = fuente_r.render(rempty, True, NEGRO)
                    texto_zona = fuente_p.render(Z9, True, BLANCO)
                elif indice_pregunta == 21:
                    texto_pregunta = fuente_p.render(p21, True, NEGRO)
                    renderizar_texto_con_saltos(p21_1, (400, 185))
                    renderizar_texto_con_saltos(p21_2, (400, 220))
                    renderizar_texto_con_saltos(p21_3, (400, 255))
                    respuestaizq = fuente_r.render(rempty, True, NEGRO)
                    respuestader = fuente_r.render(rempty, True, NEGRO)
                    texto_zona = fuente_p.render(Z9, True, BLANCO)
                elif indice_pregunta == 22:
                    texto_pregunta = fuente_p.render(p22, True, NEGRO)
                    renderizar_texto_con_saltos(p22_1, (385, 185))
                    renderizar_texto_con_saltos(p22_2, (385, 220))
                    renderizar_texto_con_saltos(p22_2_1, (385, 255))
                    respuestaizq = fuente_r.render(rempty, True, NEGRO)
                    respuestader = fuente_r.render(rempty, True, NEGRO)
                    texto_zona = fuente_p.render(Z9, True, BLANCO)
                elif indice_pregunta == 22_3:
                    texto_pregunta = fuente_p.render(p22_3, True, NEGRO)
                    renderizar_texto_con_saltos(p22_4, (400, 185))
                    renderizar_texto_con_saltos(p22_5, (400, 220))
                    respuestaizq = fuente_r.render(r39, True, NEGRO)
                    renderizar_texto_con_saltos_r(r39_1, (430, 450))
                    respuestader = fuente_r.render(r39, True, NEGRO)
                    renderizar_texto_con_saltos_r(r39_1, (695, 450))
                    texto_zona = fuente_p.render(Z9, True, BLANCO)
                    pantalla.blit(alienpng, (795, 255))
                    pantalla.blit(desc_alien, (550, 665))
                elif indice_pregunta == 23:
                    texto_pregunta = fuente_p.render(p23, True, NEGRO)
                    renderizar_texto_con_saltos(p23_1, (400, 185))
                    respuestaizq = fuente_r.render(r35, True, NEGRO)
                    respuestader = fuente_r.render(r36, True, NEGRO)
                    renderizar_texto_con_saltos_r(r36_1, (695, 450))
                    renderizar_texto_con_saltos_r(r36_2, (695, 475))
                    texto_zona = fuente_p.render(Z8, True, BLANCO)
                elif indice_pregunta == 24:
                    texto_pregunta = fuente_p.render(p24, True, NEGRO)
                    renderizar_texto_con_saltos(p24_1, (400, 185))
                    renderizar_texto_con_saltos(p24_2, (400, 220))
                    respuestaizq = fuente_r.render(r37, True, NEGRO)
                    renderizar_texto_con_saltos_r(r37_1, (430, 450))
                    renderizar_texto_con_saltos_r(r37_2, (430, 475))
                    respuestader = fuente_r.render(r38, True, NEGRO)
                    renderizar_texto_con_saltos_r(r38_1, (695, 450))
                    texto_zona = fuente_p.render(Z8, True, BLANCO)
                elif indice_pregunta == 25:
                    texto_pregunta = fuente_p.render(p25, True, NEGRO)
                    renderizar_texto_con_saltos(p25_1, (400, 185))
                    renderizar_texto_con_saltos(p25_2, (400, 220))
                    renderizar_texto_con_saltos(p25_3, (400, 255))
                    respuestaizq = fuente_r.render(rempty, True, NEGRO)
                    respuestader = fuente_r.render(rempty, True, NEGRO)
                    texto_zona = fuente_p.render(Z6, True, BLANCO)
                    pantalla.blit(gustabopng, (795, 255))
                    pantalla.blit(desc_gustabo, (520, 665))
                elif indice_pregunta == 26:
                    texto_pregunta = fuente_p.render(p26, True, NEGRO)
                    renderizar_texto_con_saltos(p26_1, (400, 185))
                    renderizar_texto_con_saltos(p26_2, (400, 220))
                    respuestaizq = fuente_r.render(rempty, True, NEGRO)
                    respuestader = fuente_r.render(rempty, True, NEGRO)
                    texto_zona = fuente_p.render(Z6, True, BLANCO)
                    pantalla.blit(gustabopng, (795, 255))
                    pantalla.blit(desc_gustabo, (520, 665))
                elif indice_pregunta == 27:
                    texto_pregunta = fuente_p.render(p27, True, NEGRO)
                    renderizar_texto_con_saltos(p27_1, (400, 185))
                    respuestaizq = fuente_r.render(rempty, True, NEGRO)
                    respuestader = fuente_r.render(rempty, True, NEGRO)
                    texto_zona = fuente_p.render(Z6, True, BLANCO)
                    pantalla.blit(gustabopng, (795, 255))
                    pantalla.blit(desc_gustabo, (520, 665))
                elif indice_pregunta == 28:
                    texto_pregunta = fuente_p.render(p28, True, NEGRO)
                    renderizar_texto_con_saltos(p28_1, (400, 185))
                    renderizar_texto_con_saltos(p28_2, (400, 220))
                    respuestaizq = fuente_r.render(rempty, True, NEGRO)
                    respuestader = fuente_r.render(rempty, True, NEGRO)
                    texto_zona = fuente_p.render(Z6, True, BLANCO)
                    pantalla.blit(gustabopng, (795, 255))
                    pantalla.blit(desc_gustabo, (520, 665))
                elif indice_pregunta == 29:
                    texto_pregunta = fuente_p.render(p29, True, NEGRO)
                    renderizar_texto_con_saltos(p29_1, (400, 185))
                    respuestaizq = fuente_r.render(r40, True, NEGRO)
                    renderizar_texto_con_saltos_r(r40_1, (430, 450))
                    renderizar_texto_con_saltos_r(r40_2, (430, 475))
                    respuestader = fuente_r.render(r41, True, NEGRO)
                    renderizar_texto_con_saltos_r(r41_1, (695, 450))
                    renderizar_texto_con_saltos_r(r41_2, (695, 475))
                    texto_zona = fuente_p.render(Z6, True, BLANCO)
                elif indice_pregunta == 30:
                    texto_pregunta = fuente_p.render(p30, True, NEGRO)
                    renderizar_texto_con_saltos(p30_1, (385, 185))
                    renderizar_texto_con_saltos(p30_2, (385, 220))
                    respuestaizq = fuente_r.render(r42, True, NEGRO)
                    renderizar_texto_con_saltos_r(r42_1, (430, 450))
                    renderizar_texto_con_saltos_r(r42_2, (430, 475))
                    respuestader = fuente_r.render(r43, True, NEGRO)
                    renderizar_texto_con_saltos_r(r43_1, (695, 450))
                    renderizar_texto_con_saltos_r(r43_2, (695, 475))
                    renderizar_texto_con_saltos_r(r43_3, (695, 500))
                    texto_zona = fuente_p.render(Z9, True, BLANCO)
                elif indice_pregunta == 32:
                    texto_pregunta = fuente_p.render(p32, True, NEGRO)
                    renderizar_texto_con_saltos(p32_1, (400, 185))
                    renderizar_texto_con_saltos(p32_2, (400, 220))
                    respuestaizq = fuente_r.render(r44, True, NEGRO)
                    respuestader = fuente_r.render(r45, True, NEGRO)
                    texto_zona = fuente_p.render(Z10, True, BLANCO)
                elif indice_pregunta == 33:
                    texto_pregunta = fuente_p.render(p33, True, NEGRO)
                    renderizar_texto_con_saltos(p33_1, (400, 185))
                    renderizar_texto_con_saltos(p33_2, (400, 220))
                    respuestaizq = fuente_r.render(r46, True, NEGRO)
                    respuestader = fuente_r.render(r47, True, NEGRO)
                    texto_zona = fuente_p.render(Z11, True, BLANCO)
                elif indice_pregunta == 34:
                    texto_pregunta = fuente_p.render(p34, True, NEGRO)
                    renderizar_texto_con_saltos(p34_1, (400, 185))
                    respuestaizq = fuente_r.render(rempty, True, NEGRO)
                    respuestader = fuente_r.render(rempty, True, NEGRO)
                    texto_zona = fuente_p.render(Z11, True, BLANCO)
                elif indice_pregunta == 35:
                    texto_pregunta = fuente_p.render(p35, True, NEGRO)
                    renderizar_texto_con_saltos(p35_1, (400, 185))
                    renderizar_texto_con_saltos(p35_2, (400, 220))
                    respuestaizq = fuente_r.render(r48, True, NEGRO)
                    renderizar_texto_con_saltos_r(r48_1, (430, 450))
                    respuestader = fuente_r.render(r49, True, NEGRO)
                    renderizar_texto_con_saltos_r(r49_1, (695, 450))
                    texto_zona = fuente_p.render(Z11, True, BLANCO)
                elif indice_pregunta == F1:
                    texto_pregunta = fuente_p.render(F1, True, NEGRO)
                    respuestaizq = fuente_r.render(rempty, True, NEGRO)
                    respuestader = fuente_r.render(rempty, True, NEGRO)
                    texto_zona = fuente_p.render(Z12, True, BLANCO) 
                elif indice_pregunta == F2:
                    texto_pregunta = fuente_p.render(F2, True, BLANCO)
                    renderizar_texto_con_saltos(F2_1, (400, 185))
                    respuestaizq = fuente_r.render(rempty, True, BLANCO)
                    respuestader = fuente_r.render(rempty, True, BLANCO)
                    texto_zona = fuente_p.render(Z12, True, BLANCO)
                elif indice_pregunta == F3:
                    texto_pregunta = fuente_p.render(F3, True, NEGRO)
                    respuestaizq = fuente_r.render(rempty, True, NEGRO)
                    respuestader = fuente_r.render(rempty, True, NEGRO)
                    texto_zona = fuente_p.render(Z12, True, BLANCO)
                    pygame.draw.rect(pantalla, NEGRO, (0, 0, 1280, 720))
                elif indice_pregunta == F4:
                    texto_pregunta = fuente_p.render(F4, True, NEGRO)
                    renderizar_texto_con_saltos(F4_1, (400, 185))
                    respuestaizq = fuente_r.render(rempty, True, NEGRO)
                    respuestader = fuente_r.render(rempty, True, NEGRO)
                    texto_zona = fuente_p.render(Z12, True, BLANCO)
                    pygame.draw.rect(pantalla, NEGRO, (0, 0, 1280, 720))
                elif indice_pregunta == F5:
                    texto_pregunta = fuente_p.render(F5, True, NEGRO)
                    renderizar_texto_con_saltos(F5_1, (400, 185))
                    respuestaizq = fuente_r.render(rempty, True, NEGRO)
                    respuestader = fuente_r.render(rempty, True, NEGRO)
                    texto_zona = fuente_p.render(Z12, True, BLANCO)
                    pygame.draw.rect(pantalla, NEGRO, (0, 0, 1280, 720))
                elif indice_pregunta == F6:
                    texto_pregunta = fuente_p.render(F6, True, NEGRO)
                    respuestaizq = fuente_r.render(rempty, True, NEGRO)
                    respuestader = fuente_r.render(rempty, True, NEGRO)
                    texto_zona = fuente_p.render(Z12, True, BLANCO)
                    pygame.draw.rect(pantalla, NEGRO, (0, 0, 1280, 720))
                elif indice_pregunta == F7:
                    texto_pregunta = fuente_p.render(F7, True, NEGRO)
                    respuestaizq = fuente_r.render(rempty, True, NEGRO)
                    respuestader = fuente_r.render(rempty, True, NEGRO)
                    texto_zona = fuente_p.render(Z12, True, BLANCO)
                if indice_pregunta == 6 or indice_pregunta == 10 or indice_pregunta == 9 or indice_pregunta == 14 or indice_pregunta == 22 or indice_pregunta == 30 or indice_pregunta == 31:
                    pantalla.blit(texto_pregunta, (385, 150))
                    pantalla.blit(respuestaizq, (430, 425))
                    pantalla.blit(respuestader, (695, 425))
                    pantalla.blit(texto_zona, (45, 655))
                else :
                    pantalla.blit(texto_pregunta, (400, 150))
                    pantalla.blit(respuestaizq, (430, 425))
                    pantalla.blit(respuestader, (695, 425))  
                    pantalla.blit(texto_zona, (45, 655))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        # inputs del juego --------- Teclas A y <- ---------------------------------------------------------------------------
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT: 
                        FX_L.play()
                        if indice_pregunta == 1: # va a la pregunta 2
                            indice_pregunta = 2
                        elif indice_pregunta == 2: # va a la pregunta 4
                            indice_pregunta = 4
                            tecnologia += 1
                        elif indice_pregunta == 3: # va a la pregunta 6
                            indice_pregunta = 6
                        elif indice_pregunta == 4: # va a la pregunta 8
                            indice_pregunta = 8
                            suministros_de_vida += 2
                            energia -= 3
                        elif indice_pregunta == 5: # va a la pregunta 9
                            indice_pregunta = 9
                            reputacion += 2
                        elif indice_pregunta == 6: # va a la pregunta 9
                            indice_pregunta = 9
                            reputacion + 2
                        elif indice_pregunta == 7: # va a la pregunta 9
                            indice_pregunta = 9
                            reputacion += 2
                        elif indice_pregunta == 8: # va a la pregunta 9
                            indice_pregunta = 9
                        elif indice_pregunta == 9: # va a la pregunta 10
                            indice_pregunta = 10
                            energia -= 2
                        elif indice_pregunta == 10: # va a la pregunta 12
                            indice_pregunta = 12
                        elif indice_pregunta == 11: # va a la pregunta 14
                            indice_pregunta = 14
                            tecnologia += 3
                            suministros_de_vida += 2
                        elif indice_pregunta == 12: # va a la pregunta 16
                            indice_pregunta = 16
                            reputacion += 2
                        elif indice_pregunta == 13: # va a la pregunta 12
                            indice_pregunta = 12
                        elif indice_pregunta == 14: # va a la respuesta 15
                            indice_pregunta = 10
                            energia -= 4
                            reputacion -= 4
                        elif indice_pregunta == 15: # va a la muerte F7
                            F7()
                        elif indice_pregunta == 16: # va a la pregunta 18
                            indice_pregunta = 18
                        elif indice_pregunta == 17: # va a la pregunta 21
                            indice_pregunta = 21
                        elif indice_pregunta == 18: # va a la pregunta 23
                            indice_pregunta = 23
                        elif indice_pregunta == 19: # va a la pregunta 22
                            indice_pregunta = 22
                        elif indice_pregunta == 20: # va a la pregunta 22
                            indice_pregunta = 22
                        elif indice_pregunta == 21: # va a la pregunta 22
                            indice_pregunta = 22
                        elif indice_pregunta == 22: # va a la pregunta 22_1
                            indice_pregunta = 22_3
                        elif indice_pregunta == 22_3:
                            indice_pregunta = 30
                            reputacion += 1
                        elif indice_pregunta == 23: # va a la pregunta 25
                            indice_pregunta = 25
                            reputacion += 2
                        elif indice_pregunta == 24: # va a la pregunta 27
                            indice_pregunta = 27
                            reputacion -= 5
                            suministros_de_vida += 2
                        elif indice_pregunta == 25: # va a la pregunta 29
                            indice_pregunta = 29
                        elif indice_pregunta == 26: # va a la pregunta 29
                            indice_pregunta = 29 
                        elif indice_pregunta == 27: # va a la pregunta 29
                            indice_pregunta = 29
                        elif indice_pregunta == 28: # va a la pregunta 29
                            indice_pregunta = 29
                        elif indice_pregunta == 29: # va a la muerte F1
                            f1()
                        elif indice_pregunta == 30: # va a la pregunta 29
                            indice_pregunta = 32
                            reputacion += 4
                            energia -= 2
                        elif indice_pregunta == 32:
                            f2()
                        elif indice_pregunta == 33:
                            indice_pregunta = 34
                        elif indice_pregunta == 34:
                            f3()
                        elif indice_pregunta == 35:
                            f4()
        # inputs del juego --------- Teclas D y -> ---------------------------------------------------------------------------
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        FX_R.play()
                        if indice_pregunta == 1: # va a la pregunta 3
                            indice_pregunta = 3
                        elif indice_pregunta == 2: # va a la pregunta 5
                            reputacion += 1
                            indice_pregunta = 5
                        elif indice_pregunta == 3: # va a la pregunta 7
                            indice_pregunta = 7
                        elif indice_pregunta == 4: # va a la pregunta 8
                            indice_pregunta = 8
                            tecnologia += 2
                            suministros_de_vida -= 1
                        elif indice_pregunta == 5: # va a la pregunta 9
                            indice_pregunta = 9
                            reputacion += 2
                        elif indice_pregunta == 6: # va a la pregunta 9
                            indice_pregunta = 9
                            reputacion += 2
                        elif indice_pregunta == 7: # va a la pregunta 9
                            indice_pregunta = 9
                            reputacion += 1
                        elif indice_pregunta == 8: # va a la pregunta 9
                            indice_pregunta = 9
                        elif indice_pregunta == 9: #este va a la pregunta 11
                            indice_pregunta = 11
                            reputacion += 2
                            energia -= 4
                        elif indice_pregunta == 10: # va a la pregunta 13
                            indice_pregunta = 13
                        elif indice_pregunta == 11: #este va a la pregunta 15
                            indice_pregunta = 15
                        elif indice_pregunta == 12: # va a la pregunta 20
                            indice_pregunta = 20
                            reputacion -= 1
                        elif indice_pregunta == 13: # va a la pregunta 17
                            indice_pregunta = 17
                        elif indice_pregunta == 14: # va a la muerte F6
                            f6()
                        elif indice_pregunta == 15: #este va a la pregunta 11
                            f7()
                        elif indice_pregunta == 16: # va a la pregunta 21
                            indice_pregunta = 21
                        elif indice_pregunta == 17: # va a la pregunta 21
                            indice_pregunta = 21
                            reputacion -= 1
                            tecnologia += 3
                            suministros_de_vida -= 5
                        elif indice_pregunta == 18: # va a la pregunta 24
                            indice_pregunta = 24
                        elif indice_pregunta == 19: # va a la pregunta 22
                            indice_pregunta = 22
                        elif indice_pregunta == 20: # va a la pregunta 22
                            indice_pregunta = 22
                        elif indice_pregunta == 21: # va a la pregunta 22
                            indice_pregunta = 22
                        elif indice_pregunta == 22: # va a la pregunta 22
                            indice_pregunta = 22_3
                        elif indice_pregunta == 22_3: # va a la pregunta 30
                            indice_pregunta = 30
                            reputacion += 1
                        elif indice_pregunta == 23: # va a la pregunta 26
                            indice_pregunta = 26
                            reputacion +=1
                        elif indice_pregunta == 24: # va a la pregunta 28
                            indice_pregunta = 28
                            reputacion += 4
                        elif indice_pregunta == 25: # va a la pregunta 29
                            indice_pregunta = 29
                        elif indice_pregunta == 26: # va a la pregunta 29
                            indice_pregunta = 29 
                        elif indice_pregunta == 27: # va a la pregunta 29
                            indice_pregunta = 29
                        elif indice_pregunta == 28: # va a la pregunta 29
                            indice_pregunta = 29
                        elif indice_pregunta == 29:
                            indice_pregunta = 19
                        elif indice_pregunta == 30:
                            indice_pregunta = 33
                            reputacion += 2
                            energia -= 6
                            tecnologia += 2
                        elif indice_pregunta == 32:
                            f2()
                        elif indice_pregunta == 33:
                            indice_pregunta = 35
                        elif indice_pregunta == 34:
                            f3()
                        elif indice_pregunta == 35:
                            f5()
                    elif event.key == pygame.K_ESCAPE:
                        main_menu()
                            
            
            
            teclas_presionadas = pygame.key.get_pressed()
            if teclas_presionadas[pygame.K_LEFT] or teclas_presionadas[pygame.K_a]:
                pantalla.blit(marco, (381, 328))         
            elif teclas_presionadas[pygame.K_RIGHT] or teclas_presionadas[pygame.K_d]:
                pantalla.blit(marco, (643, 328))
            pygame.display.update()
            
def f1():
    pygame.display.set_caption("Final")
    
    pixel_p_continuar_x = 630
    pixel_p_continuar_y = 590
    text_pos_p_continuar = (pixel_p_continuar_x, pixel_p_continuar_y)
    opacity = 255
    
    pixel_csj_zona_x = 270
    pixel_csj_zona_y = 680
    text_pos_csj_zona = (pixel_csj_zona_x, pixel_csj_zona_y)
    

    while True:
        pantalla.blit(F1, (0, 0))
        
        text_p_continuar = fuente_p.render("No puedes volver...", True, BLANCO)
        text_p_continuar.set_alpha(opacity)
        text_rect_p_continuar = text_p_continuar.get_rect(center=text_pos_p_continuar)
        
        pantalla.blit(text_p_continuar, text_rect_p_continuar)
        
        text_csj_zona = fuente_p.render("Presiona espacio para volver al menu", True, BLANCO)
        text_rect_csj_zona = text_csj_zona.get_rect(center=text_pos_csj_zona)
        
        pantalla.blit(text_csj_zona, text_rect_csj_zona)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main_menu()

        pygame.display.update()

def f2():
    pygame.display.set_caption("Final")
    
    pixel_p_continuar_x = 630
    pixel_p_continuar_y = 620
    text_pos_p_continuar = (pixel_p_continuar_x, pixel_p_continuar_y)
    opacity = 255
    
    pixel_csj_zona_x = 270
    pixel_csj_zona_y = 680
    text_pos_csj_zona = (pixel_csj_zona_x, pixel_csj_zona_y)
    

    while True:
        pantalla.blit(F2, (0, 0))
        
        text_p_continuar = fuente_p.render("Un antiaéreo ha destruido la nave, nadie a sobrevivido", True, BLANCO)
        text_p_continuar.set_alpha(opacity)
        text_rect_p_continuar = text_p_continuar.get_rect(center=text_pos_p_continuar)
        
        pantalla.blit(text_p_continuar, text_rect_p_continuar)
        
        text_csj_zona = fuente_p.render("Presiona espacio para volver al menu", True, BLANCO)
        text_rect_csj_zona = text_csj_zona.get_rect(center=text_pos_csj_zona)
        
        pantalla.blit(text_csj_zona, text_rect_csj_zona)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main_menu()

        pygame.display.update()

def f3():
    pygame.display.set_caption("Final")
    
    pixel_p_continuar_x = 630
    pixel_p_continuar_y = 620
    text_pos_p_continuar = (pixel_p_continuar_x, pixel_p_continuar_y)
    opacity = 255
    
    pixel_csj_zona_x = 270
    pixel_csj_zona_y = 680
    text_pos_csj_zona = (pixel_csj_zona_x, pixel_csj_zona_y)
    

    while True:
        pantalla.blit(F3, (0, 0))
        
        text_p_continuar = fuente_p.render("Los enfrentas con todo el equipo pero te exterminan", True, BLANCO)
        text_p_continuar.set_alpha(opacity)
        text_rect_p_continuar = text_p_continuar.get_rect(center=text_pos_p_continuar)
        
        pantalla.blit(text_p_continuar, text_rect_p_continuar)
        
        text_csj_zona = fuente_p.render("Presiona espacio para volver al menu", True, BLANCO)
        text_rect_csj_zona = text_csj_zona.get_rect(center=text_pos_csj_zona)
        
        pantalla.blit(text_csj_zona, text_rect_csj_zona)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main_menu()

        pygame.display.update()

def f4():
    pygame.display.set_caption("Final")
    
    pixel_p_continuar_x = 630
    pixel_p_continuar_y = 620
    text_pos_p_continuar = (pixel_p_continuar_x, pixel_p_continuar_y)
    opacity = 255
    
    pixel_csj_zona_x = 270
    pixel_csj_zona_y = 680
    text_pos_csj_zona = (pixel_csj_zona_x, pixel_csj_zona_y)
    

    while True:
        pantalla.blit(F4, (0, 0))
        
        text_p_continuar = fuente_p.render("Del puesto de investigación emergen Terminoides y te aniquilan", True, BLANCO)
        text_p_continuar.set_alpha(opacity)
        text_rect_p_continuar = text_p_continuar.get_rect(center=text_pos_p_continuar)
        
        pantalla.blit(text_p_continuar, text_rect_p_continuar)
        
        text_csj_zona = fuente_p.render("Presiona espacio para volver al menu", True, BLANCO)
        text_rect_csj_zona = text_csj_zona.get_rect(center=text_pos_csj_zona)
        
        pantalla.blit(text_csj_zona, text_rect_csj_zona)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main_menu()

        pygame.display.update()

def f5():
    pygame.display.set_caption("Final")
    
    pixel_p_continuar_x = 630
    pixel_p_continuar_y = 620
    text_pos_p_continuar = (pixel_p_continuar_x, pixel_p_continuar_y)
    opacity = 255
    
    pixel_csj_zona_x = 270
    pixel_csj_zona_y = 680
    text_pos_csj_zona = (pixel_csj_zona_x, pixel_csj_zona_y)
    

    while True:
        pantalla.blit(F5, (0, 0))
        
        text_p_continuar = fuente_p.render("Encuentras una horda de Terminoides y te acorralan", True, BLANCO)
        text_p_continuar.set_alpha(opacity)
        text_rect_p_continuar = text_p_continuar.get_rect(center=text_pos_p_continuar)
        
        pantalla.blit(text_p_continuar, text_rect_p_continuar)
        
        text_csj_zona = fuente_p.render("Presiona espacio para volver al menu", True, BLANCO)
        text_rect_csj_zona = text_csj_zona.get_rect(center=text_pos_csj_zona)
        
        pantalla.blit(text_csj_zona, text_rect_csj_zona)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main_menu()

        pygame.display.update()
    

def f6():
    pygame.display.set_caption("Final")
    
    pixel_p_continuar_x = 630
    pixel_p_continuar_y = 620
    text_pos_p_continuar = (pixel_p_continuar_x, pixel_p_continuar_y)
    opacity = 255
    
    pixel_csj_zona_x = 270
    pixel_csj_zona_y = 680
    text_pos_csj_zona = (pixel_csj_zona_x, pixel_csj_zona_y)
    

    while True:
        pantalla.blit(F6, (0, 0))
        
        text_p_continuar = fuente_p.render("Has muerto por pérdida de O2", True, BLANCO)
        text_p_continuar.set_alpha(opacity)
        text_rect_p_continuar = text_p_continuar.get_rect(center=text_pos_p_continuar)
        
        pantalla.blit(text_p_continuar, text_rect_p_continuar)
        
        text_csj_zona = fuente_p.render("Presiona espacio para volver al menu", True, BLANCO)
        text_rect_csj_zona = text_csj_zona.get_rect(center=text_pos_csj_zona)
        
        pantalla.blit(text_csj_zona, text_rect_csj_zona)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main_menu()

        pygame.display.update()
def f7():
    pygame.display.set_caption("Final")
    
    pixel_p_continuar_x = 630
    pixel_p_continuar_y = 620
    text_pos_p_continuar = (pixel_p_continuar_x, pixel_p_continuar_y)
    opacity = 255
    
    pixel_csj_zona_x = 270
    pixel_csj_zona_y = 680
    text_pos_csj_zona = (pixel_csj_zona_x, pixel_csj_zona_y)
    

    while True:
        pantalla.blit(F7, (0, 0))
        
        text_p_continuar = fuente_p.render("Se han perdido las coordenadas", True, BLANCO)
        text_p_continuar.set_alpha(opacity)
        text_rect_p_continuar = text_p_continuar.get_rect(center=text_pos_p_continuar)
        
        pantalla.blit(text_p_continuar, text_rect_p_continuar)
        
        text_csj_zona = fuente_p.render("Presiona espacio para volver al menu", True, BLANCO)
        text_rect_csj_zona = text_csj_zona.get_rect(center=text_pos_csj_zona)
        
        pantalla.blit(text_csj_zona, text_rect_csj_zona)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main_menu()

        pygame.display.update()
def f8():
    pygame.display.set_caption("Final")
    
    pixel_p_continuar_x = 630
    pixel_p_continuar_y = 620
    text_pos_p_continuar = (pixel_p_continuar_x, pixel_p_continuar_y)
    opacity = 255
    
    pixel_csj_zona_x = 270
    pixel_csj_zona_y = 680
    text_pos_csj_zona = (pixel_csj_zona_x, pixel_csj_zona_y)
    

    while True:
        pantalla.blit(F8, (0, 0))
        
        text_p_continuar = fuente_p.render("Te has quedado sin recursos", True, BLANCO)
        text_p_continuar.set_alpha(opacity)
        text_rect_p_continuar = text_p_continuar.get_rect(center=text_pos_p_continuar)
        
        pantalla.blit(text_p_continuar, text_rect_p_continuar)
        
        text_csj_zona = fuente_p.render("Presiona espacio para volver al menu", True, BLANCO)
        text_rect_csj_zona = text_csj_zona.get_rect(center=text_pos_csj_zona)
        
        pantalla.blit(text_csj_zona, text_rect_csj_zona)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main_menu()

        pygame.display.update()     

def creditos():
    pygame.display.set_caption("Creditos")
    
    pixel_creditos_x = 630
    pixel_creditos_y = 550
    
    text_creditos_pos = (pixel_creditos_x, pixel_creditos_y)
    opacity = 255
    
    while True:
        
        video = moviepy.editor.VideoFileClip("img/video/creditos_re.mp4")
        video.preview()
        
        text_creditos = fuente_p.render("Presiona espacio para continuar", True, (254, 110, 100))
        text_creditos_rect = text_creditos.get_rect(center=text_creditos_pos)
        
        pantalla.blit(text_creditos, text_creditos_rect)
        
        opacity -= 1.7
        if opacity <= 0:
            opacity = 255
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main_menu()

        pygame.display.update()
main_menu()
