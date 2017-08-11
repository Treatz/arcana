from evennia.commands.default.muxcommand import MuxCommand


class CmdLastBreath(MuxCommand):

    """
       +lastbreath - Determine identity and cause of corpses.
    
       Usage: 
         +lastbreath target

       Not usable on ghosts themselves.
    
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

        if not self.caller.db.spirit:
            self.caller.msg("This spell requires knowledge of the spirit sphere.")
            return
        wins = 0
        if(self.caller.db.magic_fuel):
            self.caller.msg("You roll %s dice for the spell with a difficulty of %s, using %s quintessence." % (self.caller.db.arete + self.caller.db.spirit, 6-self.caller.db.magic_fuel, self.caller.db.magic_fuel))
        else:  
            self.caller.msg("You roll %s dice for the spell with a difficulty of %s." % (self.caller.db.arete + self.caller.db.spirit, 6-self.caller.db.magic_fuel))
        for x in range(0, self.caller.db.arete + self.caller.db.spirit):
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
        hit =  self.caller.search(self.args)
        if hit.db.lastname:
            self.caller.msg("They used to be named %s." % hit.db.lastname)
            self.caller.msg("The last person to attack %s was %s." % (hit.db.lastname, hit.db.target))
        else:
              self.caller.msg("The last person to attack %s was %s." % (hit, hit.db.target))
