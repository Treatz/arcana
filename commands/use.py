from evennia.commands.default.muxcommand import MuxCommand


class CmdUse(MuxCommand):

    """
       +Use - Use luck or the luck of a charmed object.
    
       Usage: 
         +use <target>

       Can be increased if used again.
    
    """   
   
    key = "+use"
    locks = "cmd:all()"
    auto_help=False
    def func(self):
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return
        if not self.args:
            self.caller.msg("You must suply a target for the spell.")
            return

        from evennia.contrib.dice import roll_dice

        if not self.caller.db.entropy:
            self.caller.msg("This spell requires knowledge of the Entropy sphere.")
            return
        wins = 0
        for x in range(0, self.caller.db.arete):
            roll = roll_dice(1,10)
            if(roll > 5):
                wins += 1
        wins = wins + self.caller.db.entropy
        if wins < 7:
            self.caller.msg("Your spell fizzles out and fails.")
            return

        if not self.caller.db.quintessence:
            self.caller.msg("You don't have enough quintessence for that!")
            return
        else:
            self.caller.db.quintessence -= 1

        if(self.args == 'luck' or self.args == 'Luck'):
            if(self.caller.db.burned <= self.caller.db.luck):
                self.caller.msg("You sacrifice some of your natural luck.")
                self.caller.db.burned = self.caller.db.burned + 1
                self.caller.db.blessed = self.caller.db.blessed + 1
            else:
                self.caller.msg("You have burned up all of your natural luck.")
            return
        hit =  self.caller.contents
        for item in hit:
            if item.key == self.args:
                if item.db.charm:
                    item.db.charm = item.db.charm - 1
                    self.caller.msg("You use some of the luck in %s." % item)
                    self.caller.db.blessed = self.caller.db.blessed + 1
                else:
                    self.caller.msg("There is no luck left in %s." % item)
            else:
                self.caller.msg("You don't have that.")
