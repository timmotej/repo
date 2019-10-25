#!/bin/env python3

from Docker import Docker, os

net=input("Give here network name, e.g. empty -> produces 'empty_net'")
network = f"{net}_net"

dict_options = {
#    "u18p3": f" -i --net={network} ",
#    "u18p3pip": f" -i --net={network} ",
#    "u18p37": f" -i --net={network} ",
#    "u18p37pip": f" -i --net={network} ",
#    "c7p3": f" -i --net={network} ",
    "scratch": f" -i --net={network} ",
}

container = Docker(list(dict_options.keys()), network, dict_options)

container.rebuild_container()

[print("docker logs " + name) for name in dict_options.keys()]
[(print(f"\n\ndocker logs {name}\n\n"),os.system("docker logs " + name)) for name in dict_options.keys()]

print("\n\nStatus of docker containers:\n\n")
os.system("docker ps -a")
