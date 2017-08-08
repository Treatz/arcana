from evennia import default_cmds


class CmdBug(default_cmds.MuxCommand):
    """
       +Bug - Listen to everything another character says.
    
       Usage: 
        +bug <character> 
    
       Listen to another player without their knowledge.
    
    """
    key = "+bug"
    locks = "cmd:all()"
    auto_help=False
    def func(self):
        """confirms the target and initiates the search"""
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return
        # save the target object onto the command
        # this will use Evennia's default multimatch handling if more than one object matches
        target = self.caller.search(self.args, global_search=True)
        self.caller.msg("You are listening to %s." % target)
        # initialize a list to store rooms we've visited
        target.db.spy = self.caller
        
