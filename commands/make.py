from evennia.commands.default.muxcommand import MuxCommand
from evennia import create_object


class CmdMake(MuxCommand):

    """
       +make - Create objects.
    
       Usage: 
         +make <object>

       Can make any basic object..
    
    """   
    ITEM_TYPES = ('Axe', 'Knife', 'Bat', 'Staff', 'Sword')
   
    key = "+make"
    locks = "cmd:all()"
    auto_help=False
    def func(self):
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return
        if not self.args:
            self.caller.msg("You must suply a target for the spell.")
            return
	args = self.args.capitalize()
	if args not in self.ITEM_TYPES:
		self.caller.msg("It must be one of the following: %s" % ", ".join(self.ITEM_TYPES))
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

        if not self.caller.db.quintessence:
            self.caller.msg("You don't have enough quintessence for that!")
            return
        else:
            self.caller.db.quintessence -= 1
	new_object = create_object("typeclasses.objects.Object",  key=args, location=self.caller)
	self.caller.msg("You now have %s." % new_object.key)
