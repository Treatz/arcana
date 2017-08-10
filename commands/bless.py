from evennia.commands.default.muxcommand import MuxCommand

class CmdBless(MuxCommand):

    """
       +Bless - Increases your luck at everything.
    
       Usage: 
         +bless <target>

       Can be increased if used again.
    
    """   
   
    key = "+bless"
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
                if hit.db.blssed >= 0:
                   hit.db.blessed = hit.db.blessed +1
                   hit.msg("You are blessed")
                elif hit.db.blessed < 0:
                    hit.db.blessed = 0
                    hit.msg("You are no loner hexed")
        if not self.caller == hit:
               if hit.db.blessed >= 0:
                  hit.db.blessed = hit.db.blessed + 1
                  self.caller.msg("You bless %s." % hit)
                  hit.msg("You are blessed")
               elif hit.db.blessed < 0:
                   hit.db.blessed = 0
                   hit.msg("You are no longer hexed")
                   self.caller.msg("%s is no longer blessed." % hit)
