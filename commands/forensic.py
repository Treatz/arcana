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
        if hit.db.lastname:
            self.caller.msg("They used to be named %s." % hit.db.lastname)
            self.caller.msg("The last person to attack %s was %s." % (hit.db.lastname, hit.db.target))
        else:
              self.caller.msg("The last person to attack %s was %s." % (hit, hit.db.target))
