import netmiko

vyos_router = {
    'device_type': 'vyos',
    'host': '192.168.56.101',
    'username': 'kelaves',
    'key_file': 'id_rsa',
    'port': 22,
}



net_connect = netmiko.ConnectHandler(**vyos_router)

config_commands = [
    'set interfaces ethernet eth0 description eris',
]

output = net_connect.send_config_set(config_commands, exit_config_mode=False)
print(output)

output = net_connect.commit()
print(output)

output = net_connect.send_command('run show interfaces')
print(output)
