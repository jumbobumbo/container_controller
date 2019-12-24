from common.config_reader import ReturnConfDict
from common.mc_connect import McConn

# config data we are using (blank means default)
config = ReturnConfDict().json_data

# TODO: check active containers - subprocess

# do we have any active players?
player_count = McConn(config["mc_server"]["ip"], config["mc_server"]["port"]).return_act_player_num()
