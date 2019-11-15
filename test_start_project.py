#!/bin/env python3

from Docker import Docker, os

net=input("Give here network name, e.g. empty -> produces 'empty_net':\n")
network = f"{net}_net"

dict_options = {
    "empty": f" -it --net={network} -e UNAME=tom -e GNAME=mygroup ",
}

container = Docker(list(dict_options.keys()), network, dict_options)

container.rebuild_containers()

[print("docker logs " + name) for name in dict_options.keys()]
[(print(f"\n\ndocker logs {name}\n\n"),os.system("docker logs " + name)) for name in dict_options.keys()]

print("\n\nStatus of docker containers:\n\n")
os.system("docker ps -a")
