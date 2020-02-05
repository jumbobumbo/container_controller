from common.config_reader import ReturnConfDict
from common.enter_cmds import SendCmds as cmd
from common.mc_connect import McConn
from time import sleep


# config data we are using (mc_restart)
config = ReturnConfDict("mc_restart.json").json_data
# check container status
mc_status = cmd.term_in_return_str(config["commands"]["check_act_cont"], config["container"])

if mc_status:  # mc server is up
    num_checks = 0
    while num_checks <= 60:  # wait for up to an hour to restart the container
        # check to see if we have active players
        with McConn(config["mc_server"]["ip"], config["mc_server"]["port"]) as mc_con:
            player_count = mc_con.return_act_player_num()

        if player_count == 0:
            break  # nobody on, time to restart
        num_checks += 1
        sleep(60)  # seconds

    # pull latest image - restart container
    cmd(config["commands"]["dir"],
        config["commands"]["pull"],
        config["commands"]["down"],
        config["commands"]["up"]).send_commands()
