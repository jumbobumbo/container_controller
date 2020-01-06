from common.config_reader import ReturnConfDict
from common.enter_cmds import SendCmds as cmd


# config data we are using
config = ReturnConfDict("plex_pi_hole.json").json_data

# check container status
active_containers = cmd.return_cmd_response(config["generic_cmds"]["check_act_cont"])
plex_status = config["containers"]["plex"]["container_name"] in active_containers
ph_status = config["containers"]["pi_hole"]["container_name"] in active_containers

if not plex_status or ph_status:
    raise Exception(f"Plex up: {plex_status}, Pi hole up: {ph_status}")

# pull latest images - restart containers
for _ in [config["containers"]["plex"]["container_name"], config["containers"]["pi_hole"]["container_name"]]:
    cmd(config["containers"][_]["dir"],
        config["containers"][_]["pull"],
        config["generic_cmds"]["down"],
        config["generic_cmds"]["up"]).send_commands()
