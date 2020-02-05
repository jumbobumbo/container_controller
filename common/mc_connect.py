from mcstatus import MinecraftServer


class McConnPlayersOnline:
    def __init__(self, ip: str, port=25565):
        """
        Connects to a Minecraft instance - finds active player num
        :param ip: str
        :param port: int
        returns online player count
        """
        self.ip = ip
        self.port = port

    def __enter__(self):
        self.players = MinecraftServer(self.ip, self.port).status()
        return self.players.players.online

    def __exit__(self, exc_type, exc_val, exc_tb):
        del self.players
