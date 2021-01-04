import random

import gettext

# _ = gettext.gettext

def N_(message):
    return message

DAMAGE_PREFIX = [
    N_("The main "),
    N_("That @#$#@& "),
    N_("Our cheap "),
    N_("Darn-it captain, that "),
    N_("Yikes, the "),
    ]
DAMAGE_SUFFIX = [
    N_(" has died. We're on it!"),
    N_(" is out. We're working on it!"),
    N_(" is almost repaired!"),
    N_(" is dead."),
    N_(" is fried. Working as fast as we can!"),
    N_(" is toast. Working as fast as I can!"),
    N_(" is being replaced."),
    N_(" is dead. Please leave a message."),
    ]
DEFEAT_PREFIX = [
    N_("A defeated "),
    N_("The vengeful "),
    N_("An angry "),
    N_("The ejecting "),
    N_("A confused "),
    N_("Another "),
    N_("Yet another "),
    ]
DEFEAT_SUFFIX = [
    N_(" says: `I'll be back!`"),
    N_(" cries: ... 'a lucky shot!'"),
    N_(" sighs bitterly."),
    N_(" dies."),
    N_(" is rescued."),
    N_(" is history."),
    N_(" is no more."),
    N_(" is recycled."),
    N_(" is eliminated."),
    N_(" was aborted. Few lives, matter?"),
    N_(" ejects."),
    N_(" crew is rescued."),
    N_(" crew is spaced."),
    N_(" crew is recycled."),
    N_(" crew is recovered."),
    N_(" yells: 'thy mother mates poorly!'"),
    N_(" snarls: 'lucky shot.'"),
    N_(" laughs: 'you'll not do THAT again!'"),
    N_(" says nothing."),
    N_(" screams: 'thy father is a Targ!'"),
    N_(" yells: 'thine family eats bats!'"),
    N_(" snarls: 'thine people eat vermin!'"),
    N_(" curses: 'thy fathers spreadeth pox!'"),
    N_(" yells: 'thy mother is progressive!'"),
    ]
MISTAKES = [
    N_("... the crew was not impressed ..."),
    N_("... that's going to leave a mark ..."),
    N_("... next time carry the 1?"),
    N_("... math lives matter ..."),
    N_("... its coming out of your pay ..."),
    N_("... this is not a bumper car ..."),
    N_("... life can be tough that way ..."),
    N_("... who ordered THAT take-out?"),
    N_("... random is, what random does ..."),
    N_("... you've got their attention ..."),
    N_("... next time, just text them?"),
    N_("... how rude!"),
    N_("... yes, karma CAN hurt ..."),
    N_("... life is but a dream!"),
    N_("... game over."),
    N_("... starfleet will talk about this for years."),
    N_("... who is going to pay for that?"),
    N_("... galactic insurance premiums skyrocket ..."),
    N_("... captain goes down with the starship ..."),
    N_("... we'll notify your next-of-kin."),
    N_("... that was not in the script ..."),
    N_("... you never did THAT in the simulator ..."),
    ]

QUITS = [
    N_("-Let's call it a draw?"),
    N_("-You call yourself a 'Trekkie?"),
    N_("Kobayashi Maru. Python for you?"),
    N_("(Spock shakes his head)"),
    N_("(Duras, stop laughing!)"),
    N_("(... and the Klingons rejoice)"),
    N_("(... and our enemies, rejoice)"),
    N_("Kobayashi Maru... Got Python?"),
    N_("(Kirk shakes his head)"),
    ]

class Quips():
    
    @staticmethod
    def jibe(noun, prefix, suffix):
        prand = random.randrange(0, len(prefix))
        srand = random.randrange(0, len(suffix))
        return N_(prefix[prand]) + _(noun) + N_(suffix[srand])

    @staticmethod
    def jibe_quit():
        return N_(QUITS[random.randrange(0, len(QUITS))])
    
    @staticmethod
    def jibe_damage(noun):
        if random.randrange(0, 100) > 25:
            return N_("{noun} damaged. Repairs are underway.").format(noun=noun.capitalize())
        return Quips.jibe(noun, N_(DAMAGE_PREFIX), N_(DAMAGE_SUFFIX))
    
    @staticmethod
    def jibe_defeat(noun):
        if random.randrange(0, 100) > 25:
            return N_("Another {noun} defeated.").format(noun=noun.lower())
        return Quips.jibe(noun, N_(DEFEAT_PREFIX), N_(DEFEAT_SUFFIX))
    
    @staticmethod
    def jibe_fatal_mistake():
        return N_(MISTAKES[random.randrange(0, len(MISTAKES))])





