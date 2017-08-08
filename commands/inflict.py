from evennia.commands.default.muxcommand import MuxCommand


class CmdInflict(MuxCommand):

    """
       +Inflict - Causes harm to the living or the dead
    
       Usage: 
         +inflict <target>
   
       Can be used by ghosts to harm the living.
    
    """   

   
    key = "+inflict"
    locks = "cmd:all()"
    auto_help=False
    def func(self):
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return
        if not self.args:
            self.caller.msg("You must suply a target for the spell.")
            return
        if not self.caller.db.touch:
            self.caller.msg("You need stronger magic for that.")
            return
        hit =  self.caller.search(self.args)
        if not hit.db.alive:
            self.caller.msg("Target must be alive.")
            return
        if(hit.db.location == self.caller.db.location):
            hit.db.bashing = hit.db.bashing + 1
            self.caller.msg("You inflict 1 point of bashing damage on %s" % hit)
            hit.msg("You are struck through the spirit world and take 1 bashing damage.")
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
