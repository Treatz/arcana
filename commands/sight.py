from evennia.commands.default.muxcommand import MuxCommand


class CmdSight(MuxCommand):
    """
       +sight - Temporarily see into the spirit world.
    
       Usage: 
         +sight

       Also allows ghosts to see into the physical world.
    
    """   
    key = "+sight"
    locks = "cmd:all()"
    auto_help=False
    def func(self):
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return

        from evennia.contrib.dice import roll_dice

        if not self.caller.db.spirit:
            self.caller.msg("This spell requires knowledge of the spirit sphere.")
            return
        wins = 0
        for x in range(0, self.caller.db.arete):
            roll = roll_dice(1,10)
            if(roll > 5):
                wins += 1
        wins = wins + self.caller.db.spirit
        if wins < 7:
            self.caller.msg("Your spell fizzles out and fails.")
            return

        if not self.caller.db.quintessence:
            self.caller.msg("You don't have enough quintessence for that!")
            return
        else:
            self.caller.db.quintessence -= 1
        self.caller.db.sight = 1
        if self.caller.db.alive:
            self.caller.msg("You can now see into the spirit world.")
        else:
            self.caller.msg("You can now see into the physical world.")
