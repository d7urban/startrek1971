import Glyphs
from Quips import Quips

import gettext

# _ = gettext.gettext


class Stats():
    '''
    Reports do not generate damage.
    '''
    @staticmethod
    def show_ship_status(game):
        game.display()
        game.display(_("               Time Remaining: {time_remaining}").format(time_remaining=game.time_remaining))
        game.display(_("      Klingon Ships Remaining: {game_klingons}").format(game_klingons=game.game_map.game_klingons))
        game.display(_("                    Starbases: {game_starbases}").format(game_starbases=game.game_map.game_starbases))
        game.display(_("           Warp Engine Damage: {navigation_damage}").format(navigation_damage=game.enterprise.navigation_damage))
        game.display(_("   Short Range Scanner Damage: {short_range_scan_damage}").format(short_range_scan_damage=game.enterprise.short_range_scan_damage))
        game.display(_("    Long Range Scanner Damage: {long_range_scan_damage}").format(long_range_scan_damage=game.enterprise.long_range_scan_damage))
        game.display(_("       Shield Controls Damage: {shield_control_damage}").format(shield_control_damage=game.enterprise.shield_control_damage))
        game.display(_("         Main Computer Damage: {computer_damage}").format(computer_damage=game.enterprise.computer_damage))
        game.display(_("Photon Torpedo Control Damage: {photon_damage}").format(photon_damage=game.enterprise.photon_damage))
        game.display(_("                Phaser Damage: {phaser_damage}").format(phaser_damage=game.enterprise.phaser_damage))
        game.display()

    @staticmethod
    def show_galactic_status(game):
        game.display()
        str_ = _("| KLINGONS: {gklingons:>04} | ").format(gklingons=game.game_map.game_klingons)
        str_ += _("STARBASES: {gstarbases:>04} | ").format(gstarbases=game.game_map.game_starbases)
        str_ += _("STARS: {gstars:>04} |").format(gstars=game.game_map.game_stars)

        dots = len(str_) * '-'
        game.display(dots)
        game.display(str_)
        game.display(dots)

    @staticmethod
    def show_exit_status(game):
        if game.destroyed:
            msg = _("MISSION FAILED: SHIP DESTROYED")
            game.show_banner([msg], '!')
        elif game.enterprise.energy == 0:
            msg = _("MISSION FAILED: OUT OF ENERGY.")
            game.show_banner([msg], '!')
        elif game.game_map.game_klingons == 0:
            msg = _("MISSION ACCOMPLISHED"), _("ENEMIES DESTROYED"), _("WELL DONE!")
            game.show_banner(msg)
        elif game.time_remaining == 0:
            msg = _("MISSION FAILED: OUT OF TIME.")
            game.show_banner([msg], '!')
        else:
            ary = [_("::::::::: MISSION ABORTED :::::::::"), Quips.jibe_quit()]
            game.show_banner(ary, ':')

