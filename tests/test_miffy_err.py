from miffy_say.miffy_error import MiffyError


def test_miffy_error():
    try:
        raise MiffyError("miffy tells failure")
    except MiffyError:
        pass
