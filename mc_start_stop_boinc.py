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


if datetime.now().strftime("%H:%M:%S") < "10:00:00":  # with computing hours

    if mc_status:  # Minecraft container is up
        # do we have any active players?
        player_count = McConn(config["mc_server"]["ip"], config["mc_server"]["port"]).return_act_player_num()

        if player_count == 0 and not boinc_status:  # no active players and boinc container down
            cmd(config["commands"]["cd_dir"], config["commands"]["up"]).send_commands()

        elif player_count > 0 and boinc_status:  # active players and boinc container up
            cmd(config["commands"]["cd_dir"], config["commands"]["down"]).send_commands()

    elif not mc_status and not boinc_status:  # both containers down
        cmd(config["commands"]["cd_dir"], config["commands"]["up"]).send_commands()

elif datetime.now().strftime("%H:%M:%S") > "10:00:00" and boinc_status:  # out of daily computing time
    cmd(config["commands"]["cd_dir"], config["commands"]["down"]).send_commands()
