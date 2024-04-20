import pytest
from television import Television

# Test __init__ method
def test_tv_init():
    tv = Television()
    assert tv._Television__status == False  # Example of testing private variable
    assert tv._Television__volume == 0
    assert tv._Television__channel == 0

# Test power method
def test_tv_power():
    tv = Television()
    tv.power()
    assert tv._Television__status == True

# Test mute method
def test_tv_mute():
    tv = Television()
    tv.power()
    tv.mute()
    assert tv._Television__muted == True

# Test channel_up method
def test_tv_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert tv._Television__channel == 1

# Test channel_down method
def test_tv_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert tv._Television__channel == Television.MAX_CHANNEL

# Test volume_up method
def test_tv_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert tv._Television__volume == 1

# Test volume_down method
def test_tv_volume_down():
    tv = Television()
    tv.power()
    tv.volume_down()
    assert tv._Television__volume == Television.MIN_VOLUME


if __name__ == '__main__':
    pytest.main()
