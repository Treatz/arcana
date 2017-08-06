from evennia.commands.default.muxcommand import MuxCommand


class CmdTake(MuxCommand):
    """
       +take - Teleports an object.
    
       Usage: 
         +take <characte>,<object>    
       Takes an object from another player.
    
    """   
    key = "+take"
    locks = "cmd:all()"

    def func(self):
        if not self.lhs:
            self.msg("You must provide a target for this spell.")
            return
        if not self.rhs:
            self.msg("You need to specify an object.")
            return
        target = self.caller.search(self.lhs, global_search=True)
        item = target.search(self.rhs, global_search=False)
        self.msg("You teleport %s to you."% item)
        target.msg("You suddenlyf feel lighter.")
        item.move_to(self.caller)
