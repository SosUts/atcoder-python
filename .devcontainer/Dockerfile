FROM python:3.8.2
WORKDIR /workspaces

RUN apt update \
    && apt upgrade -y \
    && apt install -y npm nodejs lsb-release expect \
    && apt install fish -y \
    && pip3 install online-judge-tools\
    && npm install -g atcoder-cli \
    && pip3 install flake8 \
    && pip3 install autopep8 \
    && acc config default-task-choice all

COPY ./login_bk.sh ./atcoder_docker_vscode/login.sh
