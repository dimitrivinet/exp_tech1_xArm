# exp_tech1_xArm

Dependencies: Docker

To create docker container run (as sudo):

    docker build -t <image name>:<image tag> <relative path to Dockerfile>

To launch created docker container run:

    docker run --device /dev/snd -it <image name>:<image tag>


To use without docker:

- Install dependencies listed in Dockerfile

You may need to reinstall PortAudio properly. To do so run:

    sudo apt-get remove libportaudio2
    sudo apt-get install libasound2-dev
    git clone -b alsapatch https://github.com/gglockner/portaudio
    cd portaudio
    ./configure && make
    sudo make install
    sudo ldconfig
    cd ..