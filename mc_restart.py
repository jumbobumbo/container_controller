from requests import post

from time import sleep

from common.config_reader import ReturnConfDict
from common.enter_cmds import SendCmds as cmd


# config data we are using (mc_restart)
config = ReturnConfDict("mc_restart.json").json_data
# check container status
mc_status = cmd.term_in_return_str(config["commands"]["check_act_cont"], config["container"])

if mc_status:  # mc server is up
    num_checks = 0
    while num_checks <= 60:  # wait for up to an hour to restart the container
        # i'm hardcoding this because 1. I am lazy and 2, this is getting replaced soon cause its a bit shit
        ser_resp = post("http://192.168.1.210:9090/mc_status/",json={"server_1": {"host": "192.168.1.38", "ports": [25567], "stats": "full"}})
        mc_data = ser_resp.json()

        try:

            if mc_data['server_1']['25567']['num_players'] == 0:
                break  # nobody on, time to restart

        except KeyError:
            print(f"returned data isn't as expected: {mc_data}")
            raise KeyError

        num_checks += 1
        sleep(60)  # seconds

    # pull latest image - restart container
    cmd(config["commands"]["dir"],
        config["commands"]["pull"],
        config["commands"]["down"],
        config["commands"]["up"]).send_commands()

    print("MC server restarted")
