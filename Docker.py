#!/bin/env python3

import os
import sys


class Docker:
    def __init__(self, names, network=None, options=None, commands=None):
        self.names = names
        self.options = (
            {name:"" for name in self.names} if (options is None or not isinstance(options, dict)) else options
        )
        self.network = network
        self.commands = (
            {name:"" for name in self.names} if (commands is None or not isinstance(options, dict)) else 
                {name:commands[name] if name in list(commands.keys()) else "" for name in self.names} 
        )

    def debug(self):
        [print(var) for var in [self.names, self.options, self.network, self.commands]]

    def rm_network(self):
        comms = ["docker network rm " + self.network]
        return [os.system(comm) if self.network is not None else False for comm in comms]

    def create_network(self):
        comms = ["docker network create " + self.network]
        return [os.system(comm) if self.network is not None else False for comm in comms]

    def stop_containers(self):
        comms = ["docker stop " + name for name in self.names]
        return [os.system(comm) for comm in comms]

    def remove_containers(self):
        comms = ["docker rm " + name for name in self.names]
        return [os.system(comm) for comm in comms]

    def remove_images(self):
        comms = ["docker rmi " + name for name in self.names]
        return [os.system(comm) for comm in comms]

    def build_images(self):
        comms = [
            "docker build -t " + name + ":latest -f  " + name + ".Dockerfile ."
            for name in self.names
        ]
        return [os.system(comm) for comm in comms]

    def start_containers(self):
        comms = ["docker start " + name for name in self.names]
        return [os.system(comm) for comm in comms]

    def run_containers(self):
        comms = [
            f"docker run -d --name {name} {self.options[name]}  {name} {self.commands[name]}"
            for name in self.names
        ]
        [print(comm) for comm in comms]
        return [os.system(comm) for comm in comms]

    def copy_file(self, dict_comm):
        comms = [
            f"docker cp {dict_comm[name][0]} {dict_comm[name][1]}"
            for name in self.names
        ]
        [print(comm) for comm in comms]
        return [os.system(comm) for comm in comms]
        
    def run_command(self, dict_comm):
        comms = [
            f"docker exec -it {name} sh -c \" {dict_comm[name]} \""
            for name in self.names
        ]
        [print(comm) for comm in comms]
        return [os.system(comm) for comm in comms]
        

    def restart_containers(self):
        self.stop_containers()
        self.remove_containers()
        self.run_containers()

    def rebuild_container(self):
        self.stop_containers()
        self.remove_containers()
        self.rm_network()
        self.remove_images()
        self.build_images()
        self.create_network()
        self.run_containers()
