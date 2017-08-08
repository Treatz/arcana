from evennia.commands.default.muxcommand import MuxCommand


class CmdPush(MuxCommand):

    """
       +push - Increase your strength using forces.
    
       Usage: 
         +push

       Increases the forces of your strength significantly.
    
    """   
   
    key = "+push"
    locks = "cmd:all()"

    def func(self):     
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return
        self.caller.db.strength = self.caller.db.strength + 3
        self.caller.msg("You feel powerful.")
