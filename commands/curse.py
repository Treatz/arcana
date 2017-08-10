from evennia.commands.default.muxcommand import MuxCommand


class CmdCurse(MuxCommand):

    """
       +Curse - Increases any damamge the target is hit by.
    
       Usage: 
         +curse <target>

       Doesn't expire until the curse is activated.
    
    """   
   
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

        if not self.caller.db.entropy:
            self.caller.msg("This spell requires knowledge of the Entropy sphere.")
            return
        wins = 0
        for x in range(0, self.caller.db.arete):
            roll = roll_dice(1,10)
            if(roll > 5):
                wins += 1
        wins = wins + self.caller.db.entropy
        if wins < 7:
            self.caller.msg("Your spell fizzles out and fails.")
            return

        if not self.caller.db.quintessence:
            self.caller.msg("You don't have enough quintessence for that!")
            return
        else:
            self.caller.db.quintessence -= 1
        hit =  self.caller.search(self.args)

        if hit == self.caller:
            hit.msg("You are cursed")
            hit.db.cursed = hit.db.cursed + 1
        if not self.caller == hit:
            hit.db.cursed = hit.db.cursed +1
            self.caller.msg("You curse %s." % hit)
