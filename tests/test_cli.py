import json

import pytest

from main import main


def test_cli(capsys):
    assert main(["Hola mundo."]) == 0
    assert json.loads(capsys.readouterr().out)["words"] == 2


def test_cli_missing_argument():
    with pytest.raises(SystemExit) as error:
        main([])
    assert error.value.code == 2


def test_cli_help(capsys):
    with pytest.raises(SystemExit) as error:
        main(["--help"])
    assert error.value.code == 0
    assert "Texto entre comillas" in capsys.readouterr().out
