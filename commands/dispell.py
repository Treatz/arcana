from evennia.commands.default.muxcommand import MuxCommand


class CmdDispell(MuxCommand):

    """
       +Dispell - Stops a character from using magic.
    
       Usage: 
         +Dispell <target>
   
       Stops a character from using magic.
    
    """   

   
    key = "+dispell"
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
        if(hit.db.location == self.caller.db.location):
            hit.db.magic = 0
            self.caller.msg("You stop %s from using magic" % hit)
            hit.msg("%s has stopped you from using magic." % self.caller)
        else:
            self.caller.msg("You can't find them here.")

