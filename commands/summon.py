from evennia.commands.default.muxcommand import MuxCommand


class CmdSummon(MuxCommand):
    """
       +summon - Opens a room to the spirit world.
    
       Usage: 
         +summon    
       Allows ghosts and people in a room to hold an audience.
    
    """   
    key = "+summon"
    locks = "cmd:all()"
    auto_help=False
    def func(self):
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return

        from evennia.contrib.dice import roll_dice

        if not self.caller.db.spirit:
            self.caller.msg("This spell requires knowledge of the spirit sphere.")
            return
        wins = 0
        if(self.caller.db.magic_fuel):
            self.caller.msg("You roll %s dice for the spell with a difficulty of %s, using %s quintessence." % (self.caller.db.arete + self.caller.db.spirit, 6-self.caller.db.magic_fuel, self.caller.db.magic_fuel))
        else:  
            self.caller.msg("You roll %s dice for the spell with a difficulty of %s." % (self.caller.db.arete + self.caller.db.spirit, 6-self.caller.db.magic_fuel))
        for x in range(0, self.caller.db.arete + self.caller.db.spirit):
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
        players = [con for con in self.caller.location.contents if con.has_player]
        for player in players:
            if(player.db.alive == 1):
                player.msg("The spirit world is drawing closer.")
            if(player.db.alive == 0):
                player.msg("The physical plane is drawing closer.")
            player.db.sight = 1
            player.db.touch = 1        
