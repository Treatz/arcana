from evennia.commands.default.muxcommand import MuxCommand


class CmdRaise(MuxCommand):

    """
       +Raise - Brings a corpse back to life.
    
       Usage: 
         +raise target

       The spirit must also be nearby.
    
    """   
   
    key = "+raise"
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

        if not self.caller.db.life:
            self.caller.msg("This spell requires knowledge of the life sphere.")
            return
        wins = 0
        if(self.caller.db.magic_fuel):
            self.caller.msg("You roll %s dice for the spell with a difficulty of %s, using %s quintessence." % (self.caller.db.arete + self.caller.db.life, 6-self.caller.db.magic_fuel, self.caller.db.magic_fuel))
        else:  
            self.caller.msg("You roll %s dice for the spell with a difficulty of %s." % (self.caller.db.arete + self.caller.db.life, 6-self.caller.db.magic_fuel))
        for x in range(0, self.caller.db.arete + self.caller.db.life):
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
        hit =  self.caller.search(self.args, global_search=True)
        if hit.db.lastname:
            spirit = self.caller.search(hit.db.lastname)
            spirit.db.bashing = 0
            spirit.db.lethal = 0
            spirit.db.alive = 1
            spirit.db.conscious = 1
            spirit.msg("You have rose from the dead!")
            self.caller.msg("%s has rose from the dead." % spirit)
            for item in self.caller.location.contents:
                 if (item is not self.caller) and (item is not spirit):
                      item.msg("%s has risen from the dead!." % spirit) 

        hit.delete()
