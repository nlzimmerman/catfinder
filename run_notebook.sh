#!/bin/bash

docker run -d -p 8888:8888 -m 8g --cpu-shares=2 -v $(pwd)/jup:/home/jovyan/work -v $(pwd)/data:/home/jovyan/work/data jupyter/all-spark-notebook
