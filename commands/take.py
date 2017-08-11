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
        if(self.caller.db.magic_fuel):
            self.caller.msg("You roll %s dice for the spell with a difficulty of %s, using %s quintessence." % (self.caller.db.arete + self.caller.db.correspondence, 6-self.caller.db.magic_fuel, self.caller.db.magic_fuel))
        else:  
            self.caller.msg("You roll %s dice for the spell with a difficulty of %s." % (self.caller.db.arete + self.caller.db.correspondence, 6-self.caller.db.magic_fuel))
        for x in range(0, self.caller.db.arete + self.caller.db.correspondence):
            roll = roll_dice(1,10)
            if(roll > 5 - self.caller.db.magic_fuel):
                wins += 1
        wins = wins + self.caller.db.autopoint
        if(self.caller.db.autopoint):
            self.caller.msg("You have %s successes out of 4 needed, using a point of willpower" % wins)
        else:
            self.caller.msg("You have %s successes out of 4 needed." % wins)
        self.caller.db.magic_fuel = 0
        self.caller.db.autopoint = 0
        if wins < 4:
            self.caller.msg("Your spell fizzles out and fails.")
            return
        target = self.caller.search(self.lhs, global_search=True)
        item = target.search(self.rhs, global_search=False)
        self.msg("You teleport %s to you."% item)
        target.msg("You suddenlyf feel lighter.")
        item.move_to(self.caller)
