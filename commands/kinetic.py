from evennia.commands.default.muxcommand import MuxCommand


class CmdKinetic(MuxCommand):

    """
       +kinetic - Changes unarmed attacks to lethal.
    
       Usage: 
         +kinetic

       Increases the kinetic forces of your fists.
    
    """   
   
    key = "+kinetic"
    locks = "cmd:all()"
    auto_help=False
    def func(self):     
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return
        self.caller.db.kinetic = 1
        self.caller.msg("You are full of kinetic force.")