from evennia.commands.default.muxcommand import MuxCommand


class CmdInvis(MuxCommand):
    """
       +Invis - Temporarily makes you invisible.
    
       Usage: 
         +invisible
   
       Can only be used on yourself..
    
    """   
    auto_help = True   
    key = "+invis"
    locks = "cmd:all()"
    auto_help=False
    def func(self):
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return

        from evennia.contrib.dice import roll_dice

        if not self.caller.db.mind:
            self.caller.msg("This spell requires knowledge of the mind sphere.")
            return
        wins = 0
        for x in range(0, self.caller.db.arete):
            roll = roll_dice(1,10)
            if(roll > 5):
                wins += 1
        wins = wins + self.caller.db.mind
        if wins < 7:
            self.caller.msg("Your spell fizzles out and fails.")
            return

        if not self.caller.db.quintessence:
            self.caller.msg("You don't have enough quintessence for that!")
            return
        else:
            self.caller.db.quintessence -= 1
        self.caller.db.invis = 1
        self.caller.msg("You are now invisible.")
