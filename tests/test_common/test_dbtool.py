# from app.common.dbtool import DbTools
from .conftest import create_instance


def test_get_user(create_instance):
    """_summary_
    fixtureを使ったテスト例
    """
    # create_instanceはconftest.pyで定義したfixtureであり，これは戻り値の値db_tools_instanceを指す。
    assert create_instance.get_user() == "root"


def test_get_password(create_instance):
    """_summary_
    fixtureを使ったテスト例
    """
    assert create_instance.get_password() == "password"
