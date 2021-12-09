import netmiko
import sys

class ConfigureVyos(object):

    def __init__(self, host, user, port=22):
        self.vyos_router = {
        'device_type': 'vyos',
        'host': host,
        'username': user,
        'key_file': 'id_rsa',
        'port': port,
        }
        self.net_connect = netmiko.ConnectHandler(**self.vyos_router)
        self.command = []

    def start(self):
        option = input("configure, run command or quit? (conf/run/q): ")
        while option != 'q':
            if option == 'conf':
                self.command = []
                cmd_line = input('enter configuration(q/quit): ')
                while cmd_line not in ('q','quit'):
                    self.command += [cmd_line]
                    cmd_line = input('enter configuration(q/quit): ')
                self.config_commands()
            elif option == 'run':
                self.command = input('enter command(q/quit): ')
                while self.command not in ('q','quit'):
                    self.run_commands()
                    self.command = input('enter command(q/quit): ')
            else :
                print('Options are only "conf" and "run"')

            option = input("\nconfigure, run command or quit? (conf/run/q): ")

    def config_commands(self):
        output = self.net_connect.send_config_set(self.command, exit_config_mode=False)
        self.net_connect.commit()
        print(output)
        return output
    
    def run_commands(self):
        output = self.net_connect.send_command(self.command)
        print(output)
        return output

if __name__ == '__main__':
    host = sys.argv[1]
    user = sys.argv[2]
    vyos_2 = ConfigureVyos(host, user)
    vyos_2.start()