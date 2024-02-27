# Importieren der Pygame-Bibliothek
import pygame, math
from pygame.locals import *
import random 

# initialisieren von pygame
pygame.init()

# genutzte Farbe
ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

FENSTERBREITE = 400
FENSTERHOEHE =  800

# Fenster öffnen
screen = pygame.display.set_mode((FENSTERBREITE, FENSTERHOEHE))

# Titel für Fensterkopf
windowSurface = pygame.display.set_caption("SpaceInvaders V1.0")
spielaktiv = True

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

# Definieren der Variablen/Konstanten
Kugelpos_x = 0
Kugelpos_y = 0

KUGEL_DURCHMESSER = 15


class Raumschiff:
    def __init__ ( self, pXPos, pYPos, pXBewegung, pYBewegung ):
        self.xPos = pXPos
        self.yPos = pYPos
        self.xBewegung = pXBewegung
        self.yBewegung = pYBewegung
        

    def getXPos( self ):
        return self.xPos

    def getYPos( self ):
        return self.yPos

    def aendereBewegung(self, pXAenderung, pYAenderung):
        self.xBewegung = self.xBewegung + pXBewegungsAenderung
        self.yBewegung = self.yBewegung + pYBewegungsAenderung

    def gravity(self):
        if self.yBewegung < -0.1:
            self.yBewegung = self.yBewegung * 0,99
        elif self.yBewegung >= -0.1 and self.yBewegung <= 0:
            self.yBewegung = 0.1
        else:
            self.yBewegung = self.yBewegung / 0.99

        self.xBewegung = self.xBewegung * 0.9 + (random.randrange(-10,10,1) / 8.0 )

    def bewege( self ):
        self.gravity()
        self.xPos = self.xPos + self.xBewegung
        self.yPos = self.yPos + self.yBewegung

    def zeichne( self ):
        pygame.draw.rect(screen, ORANGE, [ self.xPos, self.yPos, 50, 10] )

    def getRect( self ):
        return Rect( [ self.xPos, self.yPos, 50, 10] )


class Kugel:
    def __init__ ( self, pXPos, pYPos, pBewegung ):
        self.xPos = pXPos
        self.yPos = pYPos
        self.bewegung = pBewegung

    def getXPos( self ):
        return self.xPos

    def getYPos( self ):
        return self.yPos

    def aendereBewegung(self, pBewegungsAenderung):
        self.bewegung = self.bewegung = + pBewegungsAenderung

    def gravity(self):
        if self.bewegung < -0.1:
            self.bewegung = self.bewegung * 0.981
        elif self.bewegung >= -0.1 and self.bewegung <= 0:
            self.bewegung = 0.1
        else:
            self.bewegung = self.bewegung / 0.981

    def bewege( self ):
        self.gravity()
        self.yPos = self.yPos + self.bewegung

    def zeichne( self ):
        pygame.draw.ellipse(screen, GRUEN, [ self.xPos +( 0.7 * KUGEL_DURCHMESSER / 2.0 ), self.yPos- 4* self.bewegung, 0.3 * KUGEL_DURCHMESSER, 0.3 * KUGEL_DURCHMESSER])
        pygame.draw.ellipse(screen, WEISS, [ self.xPos +( 0.5 * KUGEL_DURCHMESSER / 2.0 ), self.yPos- 3* self.bewegung, 0.5 * KUGEL_DURCHMESSER, 0.5 * KUGEL_DURCHMESSER])
        pygame.draw.ellipse(screen, ORANGE, [ self.xPos +( 0.3 * KUGEL_DURCHMESSER / 2.0 ), self.yPos- 2* self.bewegung, 0.7 * KUGEL_DURCHMESSER, 0.7 * KUGEL_DURCHMESSER])
        pygame.draw.ellipse(screen, ROT, [ self.xPos +( 0.1 * KUGEL_DURCHMESSER / 2.0 ), self.yPos- 1*self.bewegung, 0.9 * KUGEL_DURCHMESSER, 0.9 * KUGEL_DURCHMESSER])
        pygame.draw.ellipse(screen, WEISS, [ self.xPos, self.yPos, KUGEL_DURCHMESSER, KUGEL_DURCHMESSER])
        
    def collide( self, pRect ):
        myRect = pygame.Rect( [self.xPos, self.yPos, KUGEL_DURCHMESSER, KUGEL_DURCHMESSER])
        return myRect.colliderect( pRect )

spielfigur_1_x = 20
spielfigur_1_y = 740
spielfigur_1_bewegung = 0

listeKugeln = []
listeRaumschiffe = []

# Schleife Hauptprogramm
while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            spielaktiv = False
            print("Spieler hat Quit-Button angeklickt")
        if event.type == pygame.KEYDOWN:
            print("Spieler hat Taste gedrückt")

            # Taste für Spieler 1
            if event.key == pygame.K_LEFT:
                print("Spieler hat Pfeiltaste links gedrückt")
                spielfigur_1_bewegung = -6
            elif event.key == pygame.K_RIGHT:
                print("Spieler hat Pfeiltaste rechts gedrückt")
                spielfigur_1_bewegung = +6
            elif event.key == pygame.K_SPACE:
                listeKugeln.append( Kugel( spielfigur_1_x, spielfigur_1_y, -14 ))
                print("Anzahl Kugeln: " + str(len(listeKugeln)))
                print( listeKugeln )
##            elif event.key == pygame.K_a:
##                listeRaumschiffe.append( Raumschiff( 200, 5, 0, 1 ))
##                print("Anzahl Raumschiffe: " + str(len(listeRaumschiffe)))
##                print( listeRaumschiffe )


        # zum Stoppen der Spielerbewegung
        if event.type == pygame.KEYUP:
            print("Spieler hat Taste losgelassen")

            # Tasten für Spieler 1
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Spieler 1 stoppt bewegung")
                spielfigur_1_bewegung = 0


    # Spiellogik
    if spielfigur_1_bewegung != 0:
        spielfigur_1_x += spielfigur_1_bewegung

    if spielfigur_1_x < 0:
        spielfigur_1_x = 0

    if spielfigur_1_x > FENSTERBREITE - 60:
        spielfigur_1_x = FENSTERBREITE - 60


    if( random.randrange(0,50,1) == 1 ):
        listeRaumschiffe.append( Raumschiff( 200, 5, 0, 1 ))


    for kugel in listeKugeln:
        kugel.bewege()
        if kugel.getYPos() < 0 or kugel.getYPos() > 800:
            listeKugeln.remove(kugel)
          
    for raumschiff in listeRaumschiffe:
        raumschiff.bewege()
        if raumschiff.getYPos() < 0 or raumschiff.getYPos() > 800:
            listeRaumschiffe.remove(raumschiff)


    for kugel in listeKugeln:
        for raumschiff in listeRaumschiffe:
            if kugel.collide( raumschiff.getRect() ):
                listeRaumschiffe.remove( raumschiff )
            
    

    
    # Spielfeld löschen
    screen.fill(SCHWARZ)

    # Spielfeld/figuren zeichnen
    for kugel in listeKugeln:
        kugel.zeichne()    

    for raumschiff in listeRaumschiffe:
        raumschiff.zeichne()    


    # -- Spielerfigur 1
    player1 = pygame.draw.rect(screen, WEISS, [spielfigur_1_x, spielfigur_1_y, 60, 15 ])


    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)

pygame.quit()
