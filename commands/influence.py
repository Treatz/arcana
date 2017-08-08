from evennia import default_cmds


class CmdCommand(default_cmds.MuxCommand):
    """
       +command - Forces a character to do something.
    
       Usage: 
        +command <character> = <command>
    
       Forces someone else into doing an action.
    
    """
    key = "+Command"
    locks = "cmd:all()"
    auto_help=False
    def func(self):
        """confirms the target and initiates the search"""
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return
        # save the target object onto the command
        # this will use Evennia's default multimatch handling if more than one object matches
        self.target = self.caller.search(self.lhs, global_search=True)
        # initialize a list to store rooms we've visited
        self.target.execute_cmd(self.rhs)
        