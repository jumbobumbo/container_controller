import subprocess


class SendCmds:
    def __init__(self, *args):
        """
        :param args: lists ["your"], ["args", "here"], ["please"]
        """
        self.args = args

    @staticmethod
    def term_in_return_str(cmd, term):
        """
        checks the terminal command output for 'term' str
        :param cmd: list (containing strings) - terminal command
        :param term: term to find in string
        :return: Bool
        """
        return term in str(subprocess.check_output(cmd))

    @staticmethod
    def return_cmd_response(cmd):
        """
        :param cmd: list
        :return: response from cmd - str
        """
        return str(subprocess.check_output(cmd)).strip("'b\\")

    def send_commands(self):
        """
        send all commands from args
        """
        for cmd in self.args:
            subprocess.call(cmd)
