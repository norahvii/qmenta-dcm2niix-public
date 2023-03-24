# Install dcm2niix
# Version 24-Mar-2023
FROM centos:7

RUN yum -y update && \
    yum --enablerepo=extras install epel-release -y && \
    yum install -y wget zip unzip && \
    yum install -y epel-release && \
    yum install -y python-pip && \
    yum install -y python3-pip

# Download the 20-Jul-2022 build of dcm2niix
RUN wget -N https://github.com/rordenlab/dcm2niix/releases/download/v1.0.20220720/dcm2niix_lnx.zip -O dcm2niix_20-Jul-2022_lnx.zip

# Unzip the downloaded file to extract the dcm2niix binary
RUN unzip -o dcm2niix_20-Jul-2022_lnx.zip -d /usr/local/bin

ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# Add tool script
COPY tool.py /root/tool.py

# Install QMENTA SDK
RUN pip3 install qmenta-sdk-lib

# Configure entrypoint
RUN python3 -m qmenta.sdk.make_entrypoint /root/entrypoint.sh /root/
RUN chmod +x /root/entrypoint.sh
