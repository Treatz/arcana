from evennia.commands.default.muxcommand import MuxCommand


class CmdRaise(MuxCommand):

    """
       +Raise - Brings a corpse back to life.
    
       Usage: 
         +raise target

       The spirit must also be nearby.
    
    """   
   
    key = "+raise"
    locks = "cmd:all()"

    def func(self):
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return
        if not self.args:
            self.caller.msg("You must suply a target for the spell.")
            return
        hit =  self.caller.search(self.args, global_search=True)
        if hit.db.lastname:
            spirit = self.caller.search(hit.db.lastname)
            spirit.db.bashing = 0
            spirit.db.lethal = 0
            spirit.db.alive = 1
            spirit.db.conscious = 1
            spirit.msg("You have rose from the dead!")
            self.caller.msg("%s has rose from the dead." % spirit)
            for item in self.caller.location.contents:
                 if (item is not self.caller) and (item is not spirit):
                      item.msg("%s has risen from the dead!." % spirit) 

        hit.delete()
