from evennia.commands.default.muxcommand import MuxCommand


class CmdRaise(MuxCommand):

    """
       +Raise - Brings a corpse back to life.
    
       Usage: 
         +raise target

       The spirit must also be nearby.
    
    """   
   
    key = "+raise"
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

        if not self.caller.db.life:
            self.caller.msg("This spell requires knowledge of the life sphere.")
            return
        wins = 0
        for x in range(0, self.caller.db.arete):
            roll = roll_dice(1,10)
            if(roll > 5):
                wins += 1
        wins = wins + self.caller.db.life
        if wins < 7:
            self.caller.msg("Your spell fizzles out and fails.")
            return

        if not self.caller.db.quintessence:
            self.caller.msg("You don't have enough quintessence for that!")
            return
        else:
            self.caller.db.quintessence -= 1
        hit =  self.caller.search(self.args, global_search=True)
        if hit.db.lastname:
            spirit = self.caller.search(hit.db.lastname)
            spirit.db.bashing = 0
            spirit.db.lethal = 0
            spirit.db.alive = 1
            spirit.db.conscious = 1
            spirit.msg("You have rose from the dead!")
            self.caller.msg("%s has rose from the dead." % spirit)
            for item in self.caller.location.contents:
                 if (item is not self.caller) and (item is not spirit):
                      item.msg("%s has risen from the dead!." % spirit) 

        hit.delete()
