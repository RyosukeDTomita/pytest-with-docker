from app.mainapp.application import word, score


def test_word():
    assert word() == "hoge"


def test_score(mocker):
    mocker.patch("app.mainapp.application.random.randint", return_value=10)
    result = score()
    import app
    app.mainapp.application.random.randint.assert_called_once_with(1, 100)
    assert result == 10
