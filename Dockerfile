FROM ubuntu:20.04

RUN apt update -y

RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata git libasound2-dev gcc make

RUN git clone -b alsapatch https://github.com/gglockner/portaudio && cd portaudio && ./configure && make && make install && ldconfig && cd ..

RUN apt install -y python3-pip
RUN pip3 install speechrecognition pyaudio numpy mediapipe

RUN git clone https://github.com/xArm-Developer/xArm-Python-SDK.git && cd xArm-Python-SDK && python3 setup.py install && ldconfig

COPY /app /app

ENTRYPOINT ./app/demo_vocal_final.py

CMD bash