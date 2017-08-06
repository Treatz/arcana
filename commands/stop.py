from evennia.commands.default.muxcommand import MuxCommand


class CmdStop(MuxCommand):

    """
       +stop - Prevents attacks from hitting you.
    
       Usage: 
         +stop

       Forms energy into a invisible shield.
    
    """   
   
    key = "+stop"
    locks = "cmd:all()"

    def func(self):     
        self.caller.db.shield = 1
        self.caller.msg("You shield yourself from attacks.")
