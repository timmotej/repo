# Template for new repositories

__New repositories__ with Python scripts for starting/restarting/stopping/removing of containers contain these files:

    * `Docker.py` - Docker object with functions for calling build, start, stop, remove images
    * `[name].Dockerfile` - _[name]_ of container
    * `test_start_project.py` - rebuild and restart containers
    * `test_stop_project.py` - stopping and removing network 
