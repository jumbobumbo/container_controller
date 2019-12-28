from common.config_reader import ReturnConfDict
from common.enter_cmds import SendCmds as cmd
from common.mc_connect import McConn
from datetime import datetime

# config data we are using (blank means default)
config = ReturnConfDict().json_data
# check container status
active_containers = cmd.return_cmd_response(config["commands"]["check_act_cont"])
mc_status = config["trigger_container"] in active_containers
boinc_status = config["target_container"] in active_containers

if mc_status:  # Minecraft container is up
    # do we have any active players?
    player_count = McConn(config["mc_server"]["ip"], config["mc_server"]["port"]).return_act_player_num()

    # active players and boinc container up
    if player_count > 0 and boinc_status:
        cmd(config["commands"]["cd_dir"], config["commands"]["down"])  # take down boinc
    # no active players and boinc container down
    if player_count == 0 and not boinc_status:
        cmd(config["commands"]["cd_dir"], config["commands"]["up"])  # bring up boinc

# out of daily computing time
if datetime.now().strftime("%H:%M:%S") > "10:00:00" and boinc_status:
    cmd(config["commands"]["cd_dir"], config["commands"]["down"])  # take down boinc
