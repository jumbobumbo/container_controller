from common.enter_cmds import SendCmds as cmd

cmd("/home/jumbo", ["docker", "exec", "piholey", "pihole", "updateGravity"]).send_commands()
