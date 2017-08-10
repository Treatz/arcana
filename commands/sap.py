from evennia.commands.default.muxcommand import MuxCommand


class CmdSap(MuxCommand):

    """
       +Sap - Drains a person's physical atributes.
    
       Usage: 
         +sap <target>

       Drains a characters phsical sats.
    
    """   
   
    key = "+sap"
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
        for x in range(0, self.caller.db.arete):
            roll = roll_dice(1,10)
            if(roll > 5):
                wins += 1
        wins = wins + self.caller.db.life
        if wins < 7:
            self.caller.msg("Your spell fizzles out and fails.")
            return

        if not self.caller.db.quintessence:
            self.caller.msg("You don't have enough quintessence for that!")
            return
        else:
            self.caller.db.quintessence -= 1
        hit =  self.caller.search(self.args)
        hit.ndb.sap = 0
        if hit == self.caller:
            hit.msg("You can't sap your self.")
        if not self.caller == hit:
            hit.ndb.sap = hit.ndb.sap +1
            hit.msg("You feel tired.")
            self.caller.msg("You drain %s." % hit)
            hit.db.strength = hit.db.strength -1
            hit.db.dexterity = hit.db.dexterity -1
            hit.db.stamina - hit.db.stamina - 1
