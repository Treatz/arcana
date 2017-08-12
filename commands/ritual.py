from evennia.commands.default.muxcommand import MuxCommand
from evennia.contrib.dice import roll_dice

class CmdRitual(MuxCommand):

    """
       +Ritual - Used to start a ritual.
    
       Usage: 
         +ritual <target>
   
       Can be used before casting a spell.
    
    """   

    auto_help = False
   
    key = "+ritual"
    locks = "cmd:all()"

    def func(self):
        if not self.args:
            self.caller.msg("You must specify a focus or belief.")
            return
        if(self.caller.ndb.ritual):
            self.caller.msg("You are already doing a ritual!")
            return
        if(self.caller.db.magic_fuel > 5):
            self.caller.msg("Your magic is already fully charged.")
            return

        if(not self.caller.ndb.ritual):
            self.caller.ndb.ritual = 1
            if  self.args == "focus":
                self.caller.msg(self.caller.ndb.mefocus)
                self.caller.location.msg_contents(self.caller.ndb.roomfocus, exclude=self.caller, from_obj=self.caller)
                yield 10
                self.caller.ndb.ritual = 0
                self.caller.db.magic_fuel += 1
                self.caller.msg("You finish the ritual.")
            if self.args == "belief":
                self.caller.msg(self.caller.ndb.meritual)
                self.caller.location.msg_contents(self.caller.ndb.roomritual, exclude=self.caller, from_obj=self.caller)
                yield 10
                self.caller.ndb.ritual = 0
                self.caller.db.magic_fuel += 1
                self.caller.msg("You finish your ritual.")
