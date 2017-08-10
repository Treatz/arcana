from evennia.commands.default.muxcommand import MuxCommand


class CmdPeek(MuxCommand):
    """
       +Peek - Look at what another character is holding.
    
       Usage: 
         +peek <character>
       Peek at another characters inventory.
    
    """   
    key = "+peek"
    locks = "cmd:all()"
    auto_help=False
    def func(self):
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return

        from evennia.contrib.dice import roll_dice

        if not self.caller.db.correspondence:
            self.caller.msg("This spell requires knowledge of the correspondence sphere.")
            return
        wins = 0
        for x in range(0, self.caller.db.arete):
            roll = roll_dice(1,10)
            if(roll > 5):
                wins += 1
        wins = wins + self.caller.db.correspondence
        if wins < 7:
            self.caller.msg("Your spell fizzles out and fails.")
            return

        if not self.caller.db.quintessence:
            self.caller.msg("You don't have enough quintessence for that!")
            return
        else:
            self.caller.db.quintessence -= 1
        char =  self.caller.search(self.args)
        self.caller.msg("You peek into what %s is carrying: " % char)
        for item in char.contents:
            self.caller.msg(item) 

