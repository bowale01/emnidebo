# Use an appropriate base image
FROM ubuntu:20.04

# Install necessary packages
RUN apt-get update && apt-get install -y \
    sctp-tools \
    iproute2 \
    tcpdump \
    gcc \
    make

# Download and compile sctp_darn (or clone from a repository if available)
WORKDIR /opt
RUN git clone https://github.com/nplab/sctp_darn.git \
    && cd sctp_darn \
    && make

# Expose the SCTP port
EXPOSE 5000/sctp

# Run the SCTP server
CMD ["./sctp_darn/sctp_darn_server", "-H", "0.0.0.0", "-P", "5000"]
