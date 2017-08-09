from evennia.commands.default.muxcommand import MuxCommand


class CmdCurse(MuxCommand):

    """
       +Curse - Increases any damamge the target is hit by.
    
       Usage: 
         +curse <target>

       Doesn't expire until the curse is activated.
    
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
        if not self.caller.db.quintessence:
            self.caller.msg("You don't have enough quintessence for that!")
            return
        else:
            self.caller.db.quintessence -= 1
        hit =  self.caller.search(self.args)

        if hit == self.caller:
            hit.msg("You are cursed")
            hit.db.cursed = hit.db.cursed + 1
        if not self.caller == hit:
            hit.db.cursed = hit.db.cursed +1
            self.caller.msg("You curse %s." % hit)
