#!/bin/env python3

from Docker import Docker, os

dict_options = {
    #"sftp": f" --net={network} -v /home/timo/.ssh/id_rsa.pub:/home/foo/.ssh/keys/id_rsa.pub:ro -v /home/timo/ftp:/home/foo/share -p 2222:22 ",
    #"mariadb": f" --net={network} ",
    #"ftpd": f"--mount type=bind,src=/home/ftptest,dst=/home/ftp --mount type=bind,src=/home/timo/git/ftp-server/logs,dst=/var/log --net={network} " ,
    #"adminer" : "",
    "scratch" : "",
    #"ftpd2": f"--mount type=bind,src=/home/ftptest,dst=/home/ftp --mount type=bind,src=/home/timo/git/ftp-server/logs,dst=/var/log --net={network} -p 20-21:20-21 -p 21100-21110:21100-21110  " ,
}

first_container=list(dict_options.keys())[0]
network = os.system(f"docker inspect {first_container} -f \"{{{{json .NetworkSettings.Networks}}}}\" | cut -f1 -d: | cut -f2 -d'\"'")

dict_commands = {
    "sftp": "'foo::1001:100:upload'",
}

container = Docker(list(dict_options.keys()), network, dict_options, dict_commands)
container.stop_containers()
container.remove_containers()
container.remove_images()
container.rm_network()
#ftpd_container.debug()
#ftpd_container.restart_containers()
#ftpd_container.stop_containers()
#ftpd_container.remove_containers()
#ftpd_container.run_containers()
#
#ftpd_container.rebuild_container()

#[print("docker logs " + name) for name in dict_options.keys()]
#[(print(f"\n\ndocker logs {name}\n\n"),os.system("docker logs " + name)) for name in dict_options.keys()]

print("\n\nStatus of docker containers:\n\n")
os.system("docker ps -a")

