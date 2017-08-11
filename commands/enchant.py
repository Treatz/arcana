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
        if(self.caller.db.magic_fuel):
            self.caller.msg("You roll %s dice for the spell with a difficulty of %s, using %s quintessence." % (self.caller.db.arete + self.caller.db.matter, 6-self.caller.db.magic_fuel, self.caller.db.magic_fuel))
        else:  
            self.caller.msg("You roll %s dice for the spell with a difficulty of %s." % (self.caller.db.arete + self.caller.db.matter, 6-self.caller.db.magic_fuel))
        for x in range(0, self.caller.db.arete + self.caller.db.matter):
            roll = roll_dice(1,10)
            if(roll > 5 - self.caller.db.magic_fuel):
                wins += 1
        wins = wins + self.caller.db.autopoint
        if(self.caller.db.autopoint):
            self.caller.msg("You have %s successes out of 4 needed, using a point of willpower" % wins)
        else:
            self.caller.msg("You have %s successes out of 4 needed." % wins)
        self.caller.db.magic_fuel = 0
        self.caller.db.autopoint = 0
        if wins < 4:
            self.caller.msg("Your spell fizzles out and fails.")
            return
        hit =  self.caller.search(self.args)
        if not hit.db.enchant:
            self.caller.msg("%s has become enchanted." % hit)
            hit.db.enchant = 1
        else:
            self.caller.msg("%s has become more powerfu." % hit)
            hit.db.enchant = hit.db.enchant + 1
