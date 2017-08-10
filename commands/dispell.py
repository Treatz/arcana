from evennia.commands.default.muxcommand import MuxCommand


class CmdDispell(MuxCommand):

    """
       +Dispell - Stops a character from using magic.
    
       Usage: 
         +Dispell <target>
   
       Stops a character from using magic.
    
    """   

   
    key = "+dispell"
    locks = "cmd:all()"
    auto_help=False
    def func(self):
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return
        if not self.args:
            self.caller.msg("You must suply a target for the spell.")
            return

        from evennia.contrib.dice import roll_dice

        if not self.caller.db.prime:
            self.caller.msg("This spell requires knowledge of the Prime sphere.")
            return
        wins = 0
        for x in range(0, self.caller.db.arete):
            roll = roll_dice(1,10)
            if(roll > 5):
                wins += 1
        wins = wins + self.caller.db.prime
        if wins < 7:
            self.caller.msg("Your spell fizzles out and fails.")
            return

        if not self.caller.db.quintessence:
            self.caller.msg("You don't have enough quintessence for that!")
            return
        else:
            self.caller.db.quintessence -= 1
        hit =  self.caller.search(self.args)
        if(hit.db.location == self.caller.db.location):
            hit.db.magic = 0
            self.caller.msg("You stop %s from using magic" % hit)
            hit.msg("%s has stopped you from using magic." % self.caller)
        else:
            self.caller.msg("You can't find them here.")

