import Glyphs

import gettext

# _ = gettext.gettext


class Sector():
    def __init__(self, num=-1, name='', 
                 aliens=-1, stars=-1, 
                 starbases=-1, lines=[]):
        self.name = name
        self.number = num
        self.lines = lines
        self.area_klingons = aliens
        self.area_stars = stars
        self.area_starbases = starbases

    def is_null(self):
        return self.num == -1

    @staticmethod
    def from_area(area):
        if not area:
            return Sector()
        name = area.name
        num = area.number
        map = area.get_map()
        return Sector(num, name, 
                        area.count_glyphs(Glyphs.KLINGON),
                        area.count_glyphs(Glyphs.STAR),
                        area.count_glyphs(Glyphs.STARBASE),
                        map)


    @staticmethod                
    def display_area(game, sector):
        game.enterprise.condition = _("GREEN")
        if sector.area_klingons > 0:
            game.enterprise.condition = _("RED")
        elif game.enterprise.energy < 300:
            game.enterprise.condition = _("YELLOW")

        sb =  "     a  b  c  d  e  f  g  h \n"
        sb += _("    -=--=--=--=--=--=--=--=-             Sector: ") + sector.name + "\n"
        info = list()
        info.append(_("             Number: [{number}]\n").format(number=sector.number))
        info.append(_("           Hazzards: [{hazzards}]\n").format(hazzards=sector.area_stars + sector.area_klingons))
        info.append(_("           Stardate: {star_date}\n").format(star_date=game.star_date))
        info.append(_("          Condition: {condition}\n").format(condition=game.enterprise.condition))
        info.append(_("             Energy: {energy}\n").format(energy=game.enterprise.energy))
        info.append(_("            Shields: {shield_level}\n").format(shield_level=game.enterprise.shield_level))
        info.append(_("   Photon Torpedoes: {photon_torpedoes}\n").format(photon_torpedoes=game.enterprise.photon_torpedoes))
        info.append(_("     Time remaining: {time_remaining}\n").format(time_remaining=game.time_remaining))
        for row, line in enumerate(sector.lines):
            sb += f" {row+1} |"
            for col in line:
                sb += col
            sb += info[row]
        sb += _("    -=--=--=--=--=--=--=--=-             Docked: {docked}\n").format(docked=game.enterprise.docked)
        sb += "     a  b  c  d  e  f  g  h \n"
        print(sb, end='')

        if sector.area_klingons > 0:
            game.display()
            game.display(_("Condition RED: Klingon ship{0} detected.").format("" if sector.area_klingons == 1 else "s"))
            if game.enterprise.shield_level == 0 and not game.enterprise.docked:
                game.display(_("Warning: Shields are down."))
        elif game.enterprise.energy < 300:
            game.display()
            game.display(_("Condition YELLOW: Low energy level."))
            game.enterprise.condition = _("YELLOW")


