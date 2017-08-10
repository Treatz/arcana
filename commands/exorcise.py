from evennia.commands.default.muxcommand import MuxCommand


class CmdExorcise(MuxCommand):

    """
       +Exorcise - Send ghosts back to where they belong.
    
       Usage: +exorcise target

       Only used on dead players and ghosts.
    
    """   

   
    key = "+exorcise"
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
        hit =  self.caller.search(self.args)
        if hit:
            hit.db.conscious  = 0
            self.caller.msg("You reach across the spirit world and drain strength from %s." % hit)
            hit.msg("%s reaches across the spirit world and drains your strength." % self.caller)
        else:
            self.caller.msg("You can't sense them here.")
