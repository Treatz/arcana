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
    auto_help=False
    def func(self):     
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return
        if not self.caller.db.quintessence:
            self.caller.msg("You don't have enough quintessence for that!")
            return
        else:
            self.caller.db.quintessence -= 1
        self.caller.db.shield = 1
        self.caller.msg("You shield yourself from attacks.")
