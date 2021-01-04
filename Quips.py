import random

import gettext

# _ = gettext.gettext


DAMAGE_PREFIX = [
    _("The main "),
    _("That @#$#@& "),
    _("Our cheap "),
    _("Darn-it captain, that "),
    _("Yikes, the "),
    ]
DAMAGE_SUFFIX = [
    _(" has died. We're on it!"),
    _(" is out. We're working on it!"),
    _(" is almost repaired!"),
    _(" is dead."),
    _(" is fried. Working as fast as we can!"),
    _(" is toast. Working as fast as I can!"),
    _(" is being replaced."),
    _(" is dead. Please leave a message."),
    ]
DEFEAT_PREFIX = [
    _("A defeated "),
    _("The vengeful "),
    _("An angry "),
    _("The ejecting "),
    _("A confused "),
    _("Another "),
    _("Yet another "),
    ]
DEFEAT_SUFFIX = [
    _(" says: `I'll be back!`"),
    _(" cries: ... 'a lucky shot!'"),
    _(" sighs bitterly."),
    _(" dies."),
    _(" is rescued."),
    _(" is history."),
    _(" is no more."),
    _(" is recycled."),
    _(" is eliminated."),
    _(" was aborted. Few lives, matter?"),
    _(" ejects."),
    _(" crew is rescued."),
    _(" crew is spaced."),
    _(" crew is recycled."),
    _(" crew is recovered."),
    _(" yells: 'thy mother mates poorly!'"),
    _(" snarls: 'lucky shot.'"),
    _(" laughs: 'you'll not do THAT again!'"),
    _(" says nothing."),
    _(" screams: 'thy father is a Targ!'"),
    _(" yells: 'thine family eats bats!'"),
    _(" snarls: 'thine people eat vermin!'"),
    _(" curses: 'thy fathers spreadeth pox!'"),
    _(" yells: 'thy mother is progressive!'"),
    ]
MISTAKES = [
    _("... the crew was not impressed ..."),
    _("... that's going to leave a mark ..."),
    _("... next time carry the 1?"),
    _("... math lives matter ..."),
    _("... its coming out of your pay ..."),
    _("... this is not a bumper car ..."),
    _("... life can be tough that way ..."),
    _("... who ordered THAT take-out?"),
    _("... random is, what random does ..."),
    _("... you've got their attention ..."),
    _("... next time, just text them?"),
    _("... how rude!"),
    _("... yes, karma CAN hurt ..."),
    _("... life is but a dream!"),
    _("... game over."),
    _("... starfleet will talk about this for years."),
    _("... who is going to pay for that?"),
    _("... galactic insurance premiums skyrocket ..."),
    _("... captain goes down with the starship ..."),
    _("... we'll notify your next-of-kin."),
    _("... that was not in the script ..."),
    _("... you never did THAT in the simulator ..."),
    ]

QUITS = [
    _("-Let's call it a draw?"),
    _("-You call yourself a 'Trekkie?"),
    _("Kobayashi Maru. Python for you?"),
    _("(Spock shakes his head)"),
    _("(Duras, stop laughing!)"),
    _("(... and the Klingons rejoice)"),
    _("(... and our enemies, rejoice)"),
    _("Kobayashi Maru... Got Python?"),
    _("(Kirk shakes his head)"),
    ]

class Quips():
    
    @staticmethod
    def jibe(noun, prefix, suffix):
        prand = random.randrange(0, len(prefix))
        srand = random.randrange(0, len(suffix))
        return prefix[prand] + noun + suffix[srand]

    @staticmethod
    def jibe_quit():
        return QUITS[random.randrange(0, len(QUITS))]
    
    @staticmethod
    def jibe_damage(noun):
        if random.randrange(0, 100) > 25:
            return f"{noun.capitalize()} damaged. Repairs are underway."
        return Quips.jibe(noun, DAMAGE_PREFIX, DAMAGE_SUFFIX)
    
    @staticmethod
    def jibe_defeat(noun):
        if random.randrange(0, 100) > 25:
            return f"Another {noun.lower()} defeated."
        return Quips.jibe(noun, DEFEAT_PREFIX, DEFEAT_SUFFIX)
    
    @staticmethod
    def jibe_fatal_mistake():
        return MISTAKES[random.randrange(0, len(MISTAKES))]





