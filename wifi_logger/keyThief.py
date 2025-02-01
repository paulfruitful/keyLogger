import os
import subprocess
wifiProfiles=subprocess.check_output("netsh wlan show profile", shell=True)
wifiProfiles=wifiProfiles.splitlines()
network_names=[]

for i in wifiProfiles:
    network=i.decode('utf-8').strip()
    network=network.split(':')
    if len(network)>1:
        network_names.append(network[1])

def show_network_info(network_name):
    profile=subprocess.check_output(f'netsh wlan show profile {network_name} key=clear', shell=True)
    return profile.splitlines()

for i in network_names:
    print(f'Network {i} profile:')
    for network in network_names:
        print(f'Network {network} profile:')
        try:
            profile = show_network_info(network)  
            for info in profile:
                print(info)
        except Exception as e:
            print(f"Error fetching profile for {network}: {e}")
