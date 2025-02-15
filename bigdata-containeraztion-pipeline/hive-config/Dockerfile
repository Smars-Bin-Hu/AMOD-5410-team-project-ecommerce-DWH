FROM apache/hive
USER root
RUN apt update && apt install -y wget
# RUN wget -O jdk-8-linux-x64.tar.gz https://builds.openlogic.com/downloadJDK/openlogic-openjdk/8u272-b10/openlogic-openjdk-8u272-b10-linux-x64.tar.gz
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV PATH="$JAVA_HOME/bin:$PATH"

# overwrite entrypoint
ENTRYPOINT [ "bash", "-c", "tail -f /dev/null"]