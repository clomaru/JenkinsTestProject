FROM jenkinsci/jenkins:2.11

# install via apt
USER root

# install vim
RUN apt-get update
RUN apt-get install vim

# # install jenkins plugins
# COPY plugins.txt /usr/share/jenkins/plugins.txt
# RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt

# drop back to the regular jenkins user - good practice
USER jenkins
