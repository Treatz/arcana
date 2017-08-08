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
