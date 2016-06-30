# KATZENAUGE
# -*- coding: utf-8 -*-
from sys import exit
from random import randint

# BASE CLASS
## common things that all Scene Classes do or have
## in this case: enter()
class Scene(object):
    def enter(self):
        print "just to implement enter()..."
        exit(1)


# THE ENGINE
## Class to set up play-function, recurring to MAP-Class which is defined later

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        print "\n---------------------------------------------------------"
        print "Bei schönstem Sonnenschein schlenderst du durch einen Park."
        print "Es ist warm, die Vögel zwitschern, Eichhörnchen knabbern an Zeug."
        current_scene = self.scene_map.opening_scene()

        while True:
            #print "\n---------------------------------------------------------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)



# DEATH
## Scene to die...
class Death(Scene):

    quips = ["Tot. Das war ein ziemlich mieses Spiel...",
        "Tot. Aber wer weiss, wozu es gut ist...",
        "Tot. Bye, bye!",
        "Tot. Du bist tot. Und ein Verlierer."
        ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        print "\n"
        print "\n"
    	exit(1)

# CLOWN
## Scene to start. Later reference to Map

class Clown(Scene):

    def enter(self):
        print "Ein übergewichtiger und übellauniger Clown versperrt dir den Weg."

        action = raw_input("> ")

        talk = "reden ansprechen frage fragen unterhalten unterhalte sprech spreche rede"
        touch = "schubse schubsen rempeln schiebe schieben stoße stoßen stossen stosse fasse fassen"
        joke = "witz  Witz Witzig Lachen Lache Kitzeln joke witzig lachen lache kitzeln kitzele"

        matchtalk = list(set(action.split()) & set(talk.split()))
        matchtouch = list(set(action.split()) & set(touch.split()))
        matchjoke = list(set(action.split()) & set(joke.split()))

        if matchtalk:
            print "\n---------------------------------------------------------"
            print "Der Clown rückt mürrisch seine Nase gerade und tippt dir mit dem Zeigefinger an die Stirn."
            return 'clown'
        elif matchtouch:
            print "\n---------------------------------------------------------"
            print "Der Clown macht einen Schritt auf dich zu und reicht dir lächelnd die Hand."
            print "Dann packt er deinen Arm und zerbeisst deine Halsschlagader."
            return 'death'
        elif matchjoke:
            print "\n---------------------------------------------------------"
            print "Du erzählst deinen besten Witz in Clownsprache! HAHA!"
            print "Dabei kitzelst du den dicken Clownbauch."
            print "Der übellaunige Clown versucht mit höchster Diziplin, nicht zu lachen."
            print "Es gelingt ihm nicht. Er lacht sich tot. Der Weg ist frei..."
            print "\n"
            return 'bear'
        else:
            print "\n---------------------------------------------------------"
            print "Nja... so geht das nicht. Clowns lieben es, zu lachen. Angeblich."
            return 'clown'

# BEAR
class Bear(Scene):
    def enter(self):
        print "Du gehst weiter an einem Fluss entlang. Über den Fluss führt eine Brücke."
        print "Der Weg über die Brücke ist allerdings versperrt. Von einem weinenden Bären."
        print "Sein Einrad wurde von einem sadistischen Biber an den Brückenpfeiler geschlossen."
        print "Es handelt sich um ein dreistelliges Zahlenschloss."
        print "Mit den Zahlen 1 bis 2. TIERE!"
        print "\n"

        code = "%d%d%d" % (randint(1,2), randint(1,2), randint(1,2))
        guess = raw_input("[Zahlenschloss] > ")
        guesses = 0
        tries = 4

        while guess != code and guesses < 4:
            print "Nope!"
            print "Noch %d Versuch(e)." % tries
            print "\n"
            guesses += 1
            tries -= 1
            guess = raw_input("Zahlenschloss > ")

        if guess == code:
            print "\n---------------------------------------------------------"
            print "Das ist der Code!"
            print "Der Bär ist ein Tanzbär und tanzt glücklich mit dem Rad unter dem Arm davon..."
            print "\n"
            return 'gregor'
        else:
            print "\n---------------------------------------------------------"
            print "Tja... Bären sind keine sonderlich geduldigen Tiere..."
            print "Die Traurigkeit des Bären schlägt in blinde Wut um."
            print "Er frisst dich."
            print "\n"
            return 'death'



# GREGOR
class Gregor(Scene):
    def enter(self):
        print "An einem Schreibtisch auf einer Lichtung sitzt eine Riesenschabe."
        print "Vor ihr auf dem Tisch liegen drei halbe Walnüsse."
        print "Neben den Nüssen steht ein winziger Beamter und grinst."
        print "Die Schabe lässt den Beamten unter einer der Nüsse verschwinden"
        print "und mischt gekonnt und blitzschnell..."
        print '"Wo ist Gregor?"'
        print "\n"

        thegreg = randint(1,3)
        guess = raw_input("Nuss-Nummer > ")

        if int(guess) != 1 and int(guess) != 2 and int(guess) != 3:
            print "\n---------------------------------------------------------"
            print "Ernsthaft? Es sind DREI Nüsse..."
            print "Ja... an Dummheit KANN man sterben."
            print "\n"
            return 'death'

        elif int(guess) != thegreg:
            print "\n---------------------------------------------------------"
            print "Unter Nuss Nr. %d liegt eine grüne Murmel." % int(guess)
            print "Eine Murmel? Wo kommt die denn jetzt auf einmal her?"
            print "Auch die Schabe scheint verwirrt. Egal."
            print "Wortlos nimmst du die Murmel und gehst."
            print "\n"
            return 'cat'


        else:
            print "\n---------------------------------------------------------"
            print "Treffer bei Nuss Nr. %d" % int(guess)
            print "Der kleine Beamte stellt sich dir als Gregor Samsa vor."
            print "Erfreut schüttelst du seine winzige Hand."
            print "Gregor Samsa beisst in deinen Zeigefinger."
            print "Die Schabe und Gregor Samsa johlen und feiern. Du verblutest."
            print "\n"
            return 'death'

# CAT
class Cat(Scene):
    def enter(self):
        print "Du kommst an eine weitere Lichtung."
        print "Auf einem Stein sitzt eine einäugige Katze."
        print "Ihr noch vorhandenes Auge sieht genauso aus"
        print "wie die Murmel, die du beim Zocken gewonnen hast..."
        print "\n"

        action = raw_input("> ")
        thegreg = "murmel Murmel"
        touch = "streicheln füttere füttern kraulen Futter Fell Kraulen Streicheln Füttern futter fell streichele kraule"

        matchgreg = list(set(action.split()) & set(thegreg.split()))
        matchtouch = list(set(action.split()) & set(touch.split()))

        if matchgreg:
            print "\n---------------------------------------------------------"
            print "Ernsthaft? Du denkst, diese Murmel ist das fehlende Katzenauge?"
            print "Der Kater ist bitter enttäuscht, dass du so dreist auf seine Behinderung anspielst..."
            print "Er guckt dich einäugig so lange vorwurfsvoll an bis du stirbst."
            print "\n"
            return 'death'
        elif matchtouch:
            print "\n---------------------------------------------------------"
            print "Die Katze schnurrt und ist glücklich. Du bist glücklich."
            print "So sind Katzen eben. Und Menschen auch."
            print "HAPPY END!"
            print "\n\n\n"
            exit(1)
        else:
            return 'cat'






# MAP
## Karte der Szenen, gespeichert in einem Dict, das auf Map.scenes verweist

class Map(object):
    scenes = {
        'death': Death(),
        'clown': Clown(),
        'bear': Bear(),
        'gregor': Gregor(),
        'cat': Cat()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)


    def opening_scene(self):
        return self.next_scene(self.start_scene)



# code that runs the game by making a Map then handing that map to the engine before calling play to make the game work
a_map = Map('clown')
a_game = Engine(a_map)
a_game.play()
