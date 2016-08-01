#!/bin/bash

docker run -it -p 8889:8888 tensorflow/tensorflow
echo 'Running tensorflow Jupyter server on port 8889'
