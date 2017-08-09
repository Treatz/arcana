from evennia.commands.default.muxcommand import MuxCommand


class CmdMeditate(MuxCommand):
    """
       +Meditate - Regenerates quintessence.
    
       Usage: 
         +Meditates
   
       Can only be used on yourself..
    
    """   
    auto_help = True   
    key = "+meditate"
    locks = "cmd:all()"
    def func(self):
        if not self.caller.db.med:
            self.caller.db.med = 1
            if self.caller.db.avatar > self.caller.db.quintessence:
                self.caller.db.quintessence += 1
                self.caller.msg("You are now meditating.")
        else:
            self.caller.msg("You need to wait a while before you can do that again.")
