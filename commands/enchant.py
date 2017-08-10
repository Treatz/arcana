from evennia.commands.default.muxcommand import MuxCommand


class CmdEnchant(MuxCommand):

    """
       +enchant - blesses an object with luck.
    
       Usage: 
         +enchant <target>

       Lasts until the luck has all been exhausted.
   
    """   
   
    key = "+enchant"
    locks = "cmd:all()"
    auto_help=False
    def func(self):
        if not self.args:
            self.caller.msg("You must suply an object for the spell to work.")
            return

        from evennia.contrib.dice import roll_dice

        if not self.caller.db.matter:
            self.caller.msg("This spell requires knowledge of the matter sphere.")
            return
        wins = 0
        for x in range(0, self.caller.db.arete):
            roll = roll_dice(1,10)
            if(roll > 5):
                wins += 1
        wins = wins + self.caller.db.matter
        if wins < 7:
            self.caller.msg("Your spell fizzles out and fails.")
            return

        hit =  self.caller.search(self.args)
        if not hit.db.enchant:
            self.caller.msg("%s has become enchanted." % hit)
            hit.db.enchant = 1
        else:
            self.caller.msg("%s has become more powerfu." % hit)
            hit.db.enchant = hit.db.enchant + 1
