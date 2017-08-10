from evennia.commands.default.muxcommand import MuxCommand


class CmdCon(MuxCommand):

    """
       +Con - Examine character's physical state.
    
       Usage: 
         +con <target>

       Show physical stats..
    
    """   
   
    key = "+con"
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
            self.caller.msg("This spell requires knowledge of the Life sphere.")
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
        if not self.caller == hit:
            self.caller.msg("Strength: %s" % hit.db.strength)
            self.caller.msg("Dexterity: %s" % hit.db.dexterity)
            self.caller.msg("Stamina: %s" % hit.db.stamina)
            self.caller.msg("Bashing Damage: %s" % hit.db.bashing)
            self.caller.msg("Lethal Damage: %s" % hit.db.lethal)
            self.caller.msg("Conscious: %s" % hit.db.conscious)
            self.caller.msg("Alive: %s" % hit.db.alive)

