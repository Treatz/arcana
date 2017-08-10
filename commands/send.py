from evennia import default_cmds


class CmdSend(default_cmds.MuxCommand):
    """
       +send - Sends a message to another character with telepathy.
    
       Usage: 
        +send <character> = <message>
    
       Sends a telepathic message.
    
    """
    key = "+send"
    locks = "cmd:all()"
    auto_help=False
    def func(self):
        """confirms the target and initiates the search"""
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return

        from evennia.contrib.dice import roll_dice

        if not self.caller.db.mind:
            self.caller.msg("This spell requires knowledge of the mind sphere.")
            return
        wins = 0
        for x in range(0, self.caller.db.arete):
            roll = roll_dice(1,10)
            if(roll > 5):
                wins += 1
        wins = wins + self.caller.db.mind
        if wins < 7:
            self.caller.msg("Your spell fizzles out and fails.")
            return

        if not self.caller.db.quintessence:
            self.caller.msg("You don't have enough quintessence for that!")
            return
        else:
            self.caller.db.quintessence -= 1
        # save the target object onto the command
        # this will use Evennia's default multimatch handling if more than one object matches
        self.target = self.caller.search(self.lhs, global_search=True)
        # initialize a list to store rooms we've visited
        self.target.msg('%s speaks to you in thought, "%s"' % (self.caller.name, self.rhs))
        
