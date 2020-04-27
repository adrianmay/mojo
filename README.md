# mojo
Motion detector with velocity-of-centre-of-gravity algorithm

Many thanks to camodet_python where half of this code is copied from.

Usage:

docker build -t mojo .

docker run -it --network host -e CAM=<cam> -v /home/ad/junk:/out mojo

where <cam> is the url to the stream from a cam. Could probably be a file too. Not sure how to get at a local cam in docker.




