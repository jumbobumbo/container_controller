from datetime import datetime

from requests import post

from common.config_reader import ReturnConfDict
from common.enter_cmds import SendCmds as cmd

# config data we are using (blank means default)
config = ReturnConfDict().json_data
# check container status
active_containers = cmd.return_cmd_response(config["commands"]["check_act_cont"])
mc_status = config["trigger_container"] in active_containers
boinc_status = config["target_container"] in active_containers

cut_off = "10:30:00"
if datetime.now().strftime("%H:%M:%S") < cut_off:  # with computing hours

    if mc_status:  # Minecraft container is up
        # i'm hardcoding this because 1. I am lazy and 2, this is getting replaced soon cause its a bit shit
        ser_resp = post("http://192.168.1.210:9090/mc_status/",json={"server_1": {"host": "192.168.1.38", "ports": [25567], "stats": "full"}})
        mc_data = ser_resp.json()

        try:

            player_count = mc_data['server_1']['25567']['num_players']

        except KeyError:
            print(f"returned data isn't as expected: {mc_data}")
            raise KeyError

        if player_count == 0 and not boinc_status:  # no active players and boinc container down
            cmd(config["commands"]["dir"], config["commands"]["up"]).send_commands()

        elif player_count > 0 and boinc_status:  # active players and boinc container up
            cmd(config["commands"]["dir"], config["commands"]["down"]).send_commands()

    elif not mc_status and not boinc_status:  # both containers down
        cmd(config["commands"]["dir"], config["commands"]["up"]).send_commands()

elif datetime.now().strftime("%H:%M:%S") >= cut_off and boinc_status:  # out of daily computing time
    cmd(config["commands"]["dir"], config["commands"]["down"]).send_commands()
