#!/bin/bash

docker run -d -p 8888:8888 -m 16g --cpu-shares=4 -v $(pwd)/jup:/home/jovyan/work/jup -v $(pwd)/data:/home/jovyan/work/data -v $(pwd)/python:/home/jovyan/work/python jupyter/all-spark-notebook
