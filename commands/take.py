from evennia.commands.default.muxcommand import MuxCommand


class CmdTake(MuxCommand):
    """
       +take - Teleports an object.
    
       Usage: 
         +take <characte>,<object>    
       Takes an object from another player.
    
    """   
    key = "+take"
    locks = "cmd:all()"
    auto_help=False
    def func(self):
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return
        if not self.lhs:
            self.msg("You must provide a target for this spell.")
            return
        if not self.rhs:
            self.msg("You need to specify an object.")
            return

        from evennia.contrib.dice import roll_dice

        if not self.caller.db.correspondence:
            self.caller.msg("This spell requires knowledge of the correspondence sphere.")
            return
        wins = 0
        for x in range(0, self.caller.db.arete):
            roll = roll_dice(1,10)
            if(roll > 5):
                wins += 1
        wins = wins + self.caller.db.correspondence
        if wins < 7:
            self.caller.msg("Your spell fizzles out and fails.")
            return

        if not self.caller.db.quintessence:
            self.caller.msg("You don't have enough quintessence for that!")
            return
        else:
            self.caller.db.quintessence -= 1
        target = self.caller.search(self.lhs, global_search=True)
        item = target.search(self.rhs, global_search=False)
        self.msg("You teleport %s to you."% item)
        target.msg("You suddenlyf feel lighter.")
        item.move_to(self.caller)
