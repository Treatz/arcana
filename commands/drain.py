from evennia.commands.default.muxcommand import MuxCommand


class CmdDrain(MuxCommand):

    """
       +drain - Drains quintessence from targets willpower.
    
       Usage: 
         +drain <target>

       Target must be unconscious.
    
    """   
   
    key = "+drain"
    locks = "cmd:all()"
    auto_help=False
    def func(self):
        if self.caller.db.med:
            self.caller.msg("You are forced to stop your meditation.")
            self.caller.db.med = 0
        if self.caller.ndb.ritual:
            self.caller.msg("You are forced to stop your ritual.")
            self.caller.ndb.ritual = 0
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return
        if not self.args:
            self.caller.msg("You must suply a target for the spell.")
            return

        from evennia.contrib.dice import roll_dice

        if not self.caller.db.prime:
            self.caller.msg("This spell requires knowledge of the prime sphere.")
            return
        wins = 0
        if(self.caller.db.magic_fuel):
            self.caller.msg("You roll %s dice for the spell with a difficulty of %s, using %s quintessence." % (self.caller.db.arete + self.caller.db.prime, 6-self.caller.db.magic_fuel, self.caller.db.magic_fuel))
        else:  
            self.caller.msg("You roll %s dice for the spell with a difficulty of %s." % (self.caller.db.arete + self.caller.db.prime, 6-self.caller.db.magic_fuel))
        for x in range(0, self.caller.db.arete + self.caller.db.prime):
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

        if hit == self.caller:
            hit.msg("This doesn't work by yourself")
        if not self.caller == hit and hit.db.conscious == 0:
            hit.db.willpower = hit.db.willpower - 1
            self.caller.msg("You touch %s, charging your mana with his willpower." % hit)
            hit.msg("%s touches you, draining 1 point of willpower." % self.caller)
            self.caller.db.quintesence = self.caller.db.quintessence + 1

        detect = hit.db.perception + hit.db.awareness
        see = 0
        for x in range(1,detect):
            l = roll_dice(1,10)
            if l >= 6:
                see += 1
        if(see >= 1):
            hit.msg("%s has cast a spell on you!" % self.caller)