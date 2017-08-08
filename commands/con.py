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

    def func(self):
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return
        if not self.args:
            self.caller.msg("You must suply a target for the spell.")
            return
        hit =  self.caller.search(self.args)
        if not self.caller == hit:
            self.caller.msg("Strength: %s" % hit.db.strength)
            self.caller.msg("Dexterity: %s" % hit.db.dexterity)
            self.caller.msg("Stamina: %s" % hit.db.stamina)
            self.caller.msg("Bashing Damage: %s" % hit.db.bashing)
            self.caller.msg("Lethal Damage: %s" % hit.db.lethal)
            self.caller.msg("Conscious: %s" % hit.db.conscious)
            self.caller.msg("Alive: %s" % hit.db.alive)

