from app.common.dbtool import DbTools
import pytest


@pytest.fixture()
def create_instance():
    """_summary_
    fixtureを使ったテスト例
    """
    db_tools_instance = DbTools(user="root", password="password")
    return db_tools_instance
