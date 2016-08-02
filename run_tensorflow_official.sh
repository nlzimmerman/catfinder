#!/bin/bash

echo '----------------------------------------------'
echo 'Running tensorflow Jupyter server on port 8889'
echo '----------------------------------------------'
echo ''

docker run -it -p 8889:8888 tensorflow/tensorflow
