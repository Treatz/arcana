from evennia.commands.default.muxcommand import MuxCommand


class CmdReach(MuxCommand):
    """
       +reach - Allow players/ghosts to interact with the other's world.
    
       Usage: 
         +reach
       A temporary spell.
    
    """   
    key = "+reach"
    locks = "cmd:all()"
    auto_help=False
    def func(self):
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return
        self.caller.db.touch = 1
        if  self.caller.db.alive:
            self.caller.msg("You can now reach into the spirit world.")
        else:
            self.caller.msg("You can now reach into the physical world.")