from evennia.commands.default.muxcommand import MuxCommand


class CmdSight(MuxCommand):
    """
       +sight - Temporarily see into the spirit world.
    
       Usage: 
         +sight

       Also allows ghosts to see into the physical world.
    
    """   
    key = "+sight"
    locks = "cmd:all()"
    auto_help=False
    def func(self):
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return
        self.caller.db.sight = 1
        if self.caller.db.alive:
            self.caller.msg("You can now see into the spirit world.")
        else:
            self.caller.msg("You can now see into the physical world.")
