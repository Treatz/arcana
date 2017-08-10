from evennia.commands.default.muxcommand import MuxCommand


class CmdPush(MuxCommand):

    """
       +push - Increase your strength using forces.
    
       Usage: 
         +push

       Increases the forces of your strength significantly.
    
    """   
   
    key = "+push"
    locks = "cmd:all()"
    auto_help=False
    def func(self):     
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return


        from evennia.contrib.dice import roll_dice

        if not self.caller.db.forces:
            self.caller.msg("This spell requires knowledge of the forces sphere.")
            return
        wins = 0
        for x in range(0, self.caller.db.arete):
            roll = roll_dice(1,10)
            if(roll > 5):
                wins += 1
        wins = wins + self.caller.db.forces
        if wins < 7:
            self.caller.msg("Your spell fizzles out and fails.")
            return

        if not self.caller.db.quintessence:
            self.caller.msg("You don't have enough quintessence for that!")
            return
        else:
            self.caller.db.quintessence -= 1
        self.caller.db.strength = self.caller.db.strength + 3
        self.caller.msg("You feel powerful.")
