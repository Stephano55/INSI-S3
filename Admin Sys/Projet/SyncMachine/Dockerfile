FROM debian:bullseye

ENV DEBIAN_FRONTEND=noninteractive

# Installer les paquets nécessaires
RUN apt update && \
    apt install -y openssh-server sudo vim net-tools iputils-ping && \
    mkdir /var/run/sshd

# Créer un utilisateur personnalisé avec les droits root (UID 0, GID 0)
RUN useradd -m -u 0 -o -g 0 -s /bin/bash syncmachine && \
    echo 'syncmachine:PassSync' | chpasswd && \
    echo 'syncmachine ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# Configurer SSH pour autoriser la connexion par mot de passe
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    echo 'PermitEmptyPasswords no' >> /etc/ssh/sshd_config && \
    echo 'AllowUsers syncmachine' >> /etc/ssh/sshd_config

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
