FROM ubuntu

RUN apt-get update && apt-get install -y ansible sshpass
RUN apt-get install -y iproute2
RUN apt-get install -y openssh-server
RUN apt-get install -y nano

RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
RUN echo "AllowUsers root" >> /etc/ssh/sshd_config

RUN echo "root:root" | chpasswd

RUN mkdir ~/.ssh
RUN echo "Host *" >> ~/.ssh/config
RUN echo " StrictHostKeyChecking no" >> ~/.ssh/config