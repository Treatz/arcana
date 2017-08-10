from evennia.commands.default.muxcommand import MuxCommand


class CmdFate(MuxCommand):

    """
       +Fate - View another persons luck / karma.
    
       Usage: 
         +fate <target>

       Read another persons fate.
    
    """   
   
    key = "+fate"
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
        if hit:
            self.caller.msg("The person has charged up |g(%i) |Wpoints of karma." % int(hit.db.blessed - hit.db.cursed))
            self.caller.msg("They have used |g(%s) |Wout of |g(%s) |Wpoints of thier natural Luck." % (hit.db.burned, hit.db.Luck))
        else:
            self.caller.msg("You can't find that person.")
