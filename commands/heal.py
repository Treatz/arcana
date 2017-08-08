from evennia.commands.default.muxcommand import MuxCommand


class CmdHeal(MuxCommand):

    """
       +Heal - Restores a living being back to health.
    
       Usage: 
         +Heal <target>
   
       Cannot be used on corpses.
    
    """   

   
    key = "+heal"
    locks = "cmd:all()"

    def func(self):
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return
        if not self.args:
            self.caller.msg("You must suply a target for the spell.")
            return
        hit =  self.caller.search(self.args)
        if not hit.db.alive:
            self.caller.msg("Target must be alive.")
            return
        if(hit.db.location == self.caller.db.location):
            hit.db.bashing = 0
            hit.db.lethal = 0
            self.caller.msg("You heal all damage done to %s" % hit)
            hit.msg("%s has healed all damage done to you." % self.caller)
            healthbar = "|/|X|[wHealth:"
            total = hit.db.lethal + hit.db.bashing
            for i in range(0,8):
                if i < hit.db.lethal:
                    healthbar += " X"
                elif i < total:
                    healthbar += " /"
                else:
                    healthbar += " 0"
            healthbar += "|/"        
            hit.msg(prompt=healthbar)
        else:
            self.caller.msg("You can't find them here.")

