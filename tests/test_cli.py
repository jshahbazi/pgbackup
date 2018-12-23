import pytest

from pgbackup import cli


url = 'postgres://bob@example.com:5432/db_one'

@pytest.fixture
def parser():
    return cli.create_parser()

def test_parser_without_driver(parser):
    """
    Exit if no driver specified
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url])
        
def test_parser_with_driver(parser):
    """
    Parser exits if no destination specified
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver","local"])

def test_parser_with_unknown_driver(parser):
    """
    Parser will exit if driver name is unknown
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, '--driver','azure','destination'])
        
def test_parser_with_known_driver(parser):
    """
    Parser will not exit if driver name is known
    """
    for driver in ['local','s3']:
        assert parser.parse_args([url, '--driver', driver, 'destination'])
    
    
def test_parser_with_driver_and_destination(parser):
    """
    Parser won't exit with drive and destination
    """
    args = parser.parse_args([url, "--driver", "local", "/some/path"])

    assert args.url == url
    assert args.driver == "local"
    assert args.destination == "/some/path"