#!/bin/bash

docker run -d -p 8888:8888 -m 8g --cpu-shares=2 -v $(pwd)/jup:/home/jovyan/work/jup -v $(pwd)/data:/home/jovyan/work/data -v $(pwd)/python:/home/joyvan/work/python jupyter/all-spark-notebook
