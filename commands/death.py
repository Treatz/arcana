from evennia.commands.default.muxcommand import MuxCommand


class CmdDeathTouch(MuxCommand):

    """
       +Deathtouch - Knock a subject unconscious.
    
       Usage: 
         +deathtouch <target>

       Causes a temporary unconsciousness.
    
    """   
   
    key = "+deathtouch"
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

        hit =  self.caller.search(self.args)

        if hit == self.caller:
            hit.msg("This doesn't work by yourself")
        if not self.caller == hit:
            hit.db.lethal = hit.db.lethal + 1
            self.caller.msg("You touch %s, causing 1 point of lethal damage." % hit)
            hit.msg("%s touches you, causing 1 point of lethal damage." % self.caller)
            healthbar = "|/|X|[wHealth:"
            total = hit.db.lethal + hit.db.bashing
            for i in range(0,8):
                if i < hit.db.lethal:
                    healthbar += " X"
                elif i < total:
                    healthbar += " /"
                else:
                    healthbar += " 0"
                healthbar += "|/"        
                hit.msg(prompt=healthbar)
