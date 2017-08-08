from evennia import default_cmds


class CmdBan(default_cmds.MuxCommand):
    """
       +Ban - Bans a character from a room with bad luck.
    
       Usage: 
        +ban <character> = <room>
    
       Luck can be reginerated when you leave the room.
    
    """
    key = "+Ban"
    locks = "cmd:all()"

    def func(self):
        """confirms the target and initiates the search"""
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return
        # save the target object onto the command
        # this will use Evennia's default multimatch handling if more than one object matches
        self.target = self.caller.search(self.lhs, global_search=True)
        self.target2 = self.caller.search(self.rhs, global_search=True)
        # initialize a list to store rooms we've visited
        self.target.db.ban = self.target2
        
