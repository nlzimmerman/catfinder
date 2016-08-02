#!/bin/bash

if [ ! -f ADEChallengeData2016.zip ]; then
	wget http://sceneparsing.csail.mit.edu/data/ADEChallengeData2016.zip
fi
if [ $(sha1sum ADEChallengeData2016.zip | awk '{print $1;}') !=  "219e1696abb36c8ba3a3afe7fb2f4b4606a897c7" ]; then
	echo "ADEChallengeData2016.zip sha1sum doesn't match!!"
	exit 1
fi
if [ ! -f train.zip ]; then
	echo "You need to download train.zip from https://www.kaggle.com/c/dogs-vs-cats/data after agreeing to the license agreement."
	exit 1
fi
if [ $(sha1sum train.zip | awk '{print $1;}') != "1b888369d6d5db7e8edbc286c99739cc231d9d64" ]; then
	echo "train.zip sha1sum doesn't match!!"
	exit 1
fi
if [ ! -f test1.zip ]; then
	echo "You need to download test1.zip from https://www.kaggle.com/c/dogs-vs-cats/data after agreeing to the license agreement."
	exit 1
fi
if [ $(sha1sum test1.zip | awk '{print $1;}') != "391aa2875979d00d475196036b94a5a64e01b281" ]; then
	echo "test1.zip sha1sum doesn't match!!"
	exit 1
fi
