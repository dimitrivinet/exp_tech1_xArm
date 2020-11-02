FROM ubuntu:20.04

RUN apt update -y
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata
RUN apt install -y python3-pip libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
RUN pip3 install speechrecognition pyaudio

COPY /app /app

CMD ./app/speech_control/speech_recog.py
