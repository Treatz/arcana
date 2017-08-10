from evennia.commands.default.muxcommand import MuxCommand


class CmdKinetic(MuxCommand):

    """
       +kinetic - Changes unarmed attacks to lethal.
    
       Usage: 
         +kinetic

       Increases the kinetic forces of your fists.
    
    """   
   
    key = "+kinetic"
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
        self.caller.db.kinetic = 1
        self.caller.msg("You are full of kinetic force.")
