# pytest with docker

![un license](https://img.shields.io/github/license/RyosukeDTomita/pytest-with-docker)
[![unit-test](https://github.com/RyosukeDTomita/pytest-with-docker/actions/workflows/pytest.yml/badge.svg)](https://github.com/RyosukeDTomita/pytest-with-docker/actions/workflows/pytest.yml)

## INDEX

- [ABOUT](#about)
- [LICENSE](#license)
- [ENVIRONMENT](#environment)
- [PREPARING](#preparing)
- [HOW TO USE](#how-to-use)
- [ABOUT](#about)

---

## ABOUT
- pytestのpyファイル名は`test_application.py`のように命名する。
- pytestのpyファイルは`tests/test_mainapp`のようにする。
- 各ディレクトリに`__init__.py`を配置する。
- [pytest](https://rinatz.github.io/python-book/ch08-02-pytest/)の詳細はこちらを参照。

```
.
├── app
│   └── mainapp
│       ├── application.py
│       ├── __init__.py
│       └── __pycache__
│           ├── application.cpython-38.pyc
│           └── __init__.cpython-38.pyc
├── docker-compose.yml
├── Dockerfile
├── README.md
└── tests
    ├── __init__.py
    ├── __pycache__
    │   └── __init__.cpython-38.pyc
    └── test_mainapp
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-38.pyc
        │   └── test_application.cpython-38-PYTEST.pyc
        └── test_application.py
```

---

## LICENSE

---

[UN LICENSE](./LICENSE)

---

## ENVIRONMENT
- ubuntu22.04(docker)

---

## PREPARING
1. install docker
2. download this repository.

---

## HOW TO USE
- pythonのバージョンはDockerfileで指定しているので適宜書き換える。

```shell
docker buildx bake
docker compose run pytest-env "cd /pytest-with-docker && /pyenv/versions/3.9.6/bin/pytest
```

> [!Note]
> ローカルでpytestを実行するなら毎回docker runで無駄にコンテナを立ち上げずに起動したコンテナに対してexecでpytest実行したほうがいいかも。
> コンテナはタスクが終わると自動で終了してしまうので，DockerfileのCMDでtail -f /dev/null等してコンテナを実行したままの状態にする。
> 現状コメントアウトされているので外す(これをやるとgithub actionsで実行しているpytestが動かなくなるので注意)。

```shell
docker compose up -d
docker compose exec pytest-env /bin/bash -c "cd /pytest-with-docker && /pyenv/versions/3.9.6/bin/pytest"
```

- github actionsでも実行可能。
> [!Warning]
> CMD等でコマンドを実行するようにしてdocker compose up等するとテストの結果にかかわらず，コマンドが実行できたらステータスコードが0になるのでbuildとrunに分けている。
