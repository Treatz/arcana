from evennia.commands.default.muxcommand import MuxCommand


class CmdStrike(MuxCommand):

    """
       +Strike - Call lightning.
    
       Usage: 
         +strike <target>

       Must be used outside.
    
    """   
   
    key = "+strike"
    locks = "cmd:all()"
    auto_help=False
    def func(self):
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return
        if not self.args:
            self.caller.msg("You must suply a target for the spell.")
            return
        hit =  self.caller.search(self.args)

        if hit == self.caller:
            self.caller.msg("You don't want to do that!")
            return                

        from evennia.contrib.dice import roll_dice

        if not self.caller.db.forces:
            self.caller.msg("This spell requires knowledge of the forces sphere.")
            return
        wins = 0
        for x in range(0, self.caller.db.arete):
            roll = roll_dice(1,10)
            if(roll > 5):
                wins += 1
        wins = wins + self.caller.db.forces
        if wins < 7:
            self.caller.msg("Your spell fizzles out and fails.")
            return

        if not self.caller.db.quintessence:
            self.caller.msg("You don't have enough quintessence for that!")
            return
        else:
            self.caller.db.quintessence -= 1

        if hit:
            hit.msg("You are struck by lightning!")
            self.caller.msg("%s is truck by lightning!" % hit)                  
            hit.db.conscious = 0
            hit.db.lethal = hit.db.lethal + 4
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
