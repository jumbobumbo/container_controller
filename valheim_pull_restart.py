from common.config_reader import ReturnConfDict
from common.enter_cmds import SendCmds as cmd


if __name__ == "__main__":
    # config data we are using
    config = ReturnConfDict("valheim.json").json_data
    # pull latest image - restart container
    cmd(
        config["generic_cmds"]["pull"],
        config["generic_cmds"]["down"],
        config["generic_cmds"]["up"],
        working_dir=config["containers"]["val_1"]["dir"]
    ).send_commands()