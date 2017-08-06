from evennia.commands.default.muxcommand import MuxCommand


class CmdIllusion(MuxCommand):

    """
       +illusion - Fills the room with an illusion.
    
       Usage: 
         +Illusion

       Everyone in a room sees the illusion    
    """   
   
    key = "+illusion"
    locks = "cmd:all()"

    def func(self):     
        self.caller.msg("You create an illusion in the room:")
        self.caller.msg(self.args)
        self.caller.location.msg_contents(self.args, exclude=self.caller, from_obj=self.caller)
