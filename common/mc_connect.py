from mcstatus import MinecraftServer


class McConn:
    def __init__(self, ip: str, conn_type: str, port=25565):
        """
        Connects to a Minecraft instance
        :param ip: str
        :param conn_type: str ("tcp" or "udp")
        :param port: int
        """
        self.ip = ip
        self.conn_type = conn_type
        self.port = port

    def __enter__(self):
        self.connection = MinecraftServer(self.ip, self.port)
        return self.connection

    def return_act_player_num(self):
        """
        TCP ONLY
        :return: int - active players on server
        """
        if self.conn_type.lower() == "tcp":
            return self.connection.status().players.online

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn_type.lower() == "tcp":
            self.connection.status().socket.close()
        elif self.conn_type.lower() == "udp":
            self.connection.query().socket.close()
