from mcstatus import MinecraftServer


class McConn:
    def __init__(self, ip, port=25565):
        """
        Connects to a Minecraft instance
        :param ip: str
        :param port: int
        """
        self.ip = ip
        self.port = port

    def return_act_player_num(self):
        """
        :return: int - active players on server
        """
        return MinecraftServer(self.ip, self.port).status().players.online
