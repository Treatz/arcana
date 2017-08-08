from evennia.commands.default.muxcommand import MuxCommand


class CmdClone(MuxCommand):

    """
       +Clone - Cange your appearance into someone else.
    
       Usage: 
         +clone <target>

       Changes your appearance but not your stats.
    
    """   
   
    key = "+clone"
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
        if not hit:
            return
        if hit == self.caller:
            hit.msg("You can't clone your self.")
        if not self.caller.key == hit.key:
            self.caller.ndb.nameSave = self.caller.key
            self.caller.key = hit.key
            self.caller.ndb.descSave = self.caller.db.desc
            self.caller.db.desc = hit.db.desc
            self.caller.ndb.imageSave = self.caller.db.image
            self.caller.db.image = hit.db.image
            self.caller.msg("You now appear as %s." % self.caller.key)
            
