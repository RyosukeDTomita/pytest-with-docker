# pytestをローカルで実行したいだけの時。
# docker compose run pytest-env "/pyenv/versions/3.9.6/bin/pytest"
FROM ubuntu:22.04 as dependencies
ENV PYTHON_VERSION=3.9.6
ENV DEBIAN_FRONTEND=noninteractive
ENV PYENV_ROOT="/pyenv"
ENV PATH="$PYENV_ROOT/bin:$PATH"
SHELL ["/bin/bash", "-c"]
COPY ./requirements.txt /requirements.txt
RUN apt-get update \
    # pyenv dependencies
    && apt-get install -y \
        git \
        aria2 \
        wget \
        gcc \
        make \
        libssl-dev \
        zlib1g-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        llvm \
        libncurses5-dev \
        libncursesw5-dev \
        xz-utils \
        tk-dev \
        libffi-dev \
        liblzma-dev \
        python3-openssl \
    # tzdataにより1. Africa  2. America のような選択肢をコンソールから選択しなくていいようにあらかじめタイムゾーンを指定。
    && ln -fs /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
    && dpkg-reconfigure --frontend noninteractive tzdata \
    # pyenv setup
	&& git clone https://github.com/pyenv/pyenv.git /pyenv \
    && echo 'export PYENV_ROOT="/pyenv"' >> ~/.bashrc \
    && echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc \
    && echo 'eval "$(pyenv init -)"' >> ~/.bashrc \
    && source ~/.bashrc \
    # これをshell起動ごとにやらないとpythonのパスが通らない。
    && eval "$(pyenv init -)" \
    && pyenv install ${PYTHON_VERSION} \
    && pyenv global ${PYTHON_VERSION} \
    # pytest set up
    && apt-get install -y python3-pip \
    && cd / \
    # libmysqlclinet-devはmysqlclientをinstallするのに必要
	&& apt-get install -y libmysqlclient-dev \
	&& python -m pip install -r requirements.txt \
	&& rm -rf /var/lib/lists \
    && rm /requirements.txt


FROM dependencies AS app
COPY ./ /pytest-with-docker
ENTRYPOINT [ "/bin/bash", "-c" ]
# CMD ["tail -f /dev/null"]
