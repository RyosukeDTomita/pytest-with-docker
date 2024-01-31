import pytest
from app.mainapp.application import word, score, greeting, load_numbers_sorted


def test_word():
    assert word() == "hoge"


def test_score(mocker):
    """_summary_

    Args:
        mocker (_type_): _description_
    mockを使ったテスト例
    """
    mocker.patch("app.mainapp.application.random.randint", return_value=10)
    result = score()
    import app
    app.mainapp.application.random.randint.assert_called_once_with(1, 100)
    assert result == 10


def test_score_spy(mocker):
    """_summary_

    Args:
        mocker (_type_): _description_
    spyを使ったテスト例
    spyを使うと，mockと違いoriginalの関数を呼びつつ，呼び出し回数等を記録できる。
    """
    import app
    spy = mocker.spy(app.mainapp.application.random, "randint")
    result = score()
    spy.assert_called_once_with(1, 100)
    assert result <= 100


def test_score_out(capsys):
    """_summary_
    標準出力をテストする例
    Args:
        capsys (_type_): _description_
    """
    result = score()
    out, _ = capsys.readouterr()
    assert out == ("{}\n".format(result))


@pytest.mark.parametrize(("name", "expected"), [
    ("john", "hello john"),
    ("tom", "hello tom"),

])
def test_greeting(name, expected):
    """_summary_
    parametrizeを使ったテスト例
    """
    assert greeting(name) == expected


@pytest.fixture()
def txt(tmpdir) -> str:
    # テスト実行前にやる処理
    tmpfile = tmpdir.join("numbers.txt")
    with tmpfile.open("w") as f:
        for n in [3, 1, 2]:
            f.write('{}\n'.format(n))
    yield str(tmpfile)

    # テスト実行後の処理
    tmpfile.remove()


def test_load_numbers_sorted(txt):
    """_summary_
    tmpdirを使ったテスト例
    """
    assert load_numbers_sorted(txt) == [1, 2, 3]
