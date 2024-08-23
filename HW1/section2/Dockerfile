FROM ubuntu:22.04
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install socat
RUN useradd -m pwn
WORKDIR /home/pwn
COPY dutchman_hell_1 .
RUN echo 'CE441{some_fake_flag}' > ./flag.txt
RUN chown -R root:root /home/pwn
RUN chmod -R 555 /home/pwn
CMD ["socat", "TCP-LISTEN:5000,reuseaddr,fork", "EXEC:'timeout 60 su pwn -c ./dutchman_hell_1'"]
