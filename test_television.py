import pytest
from television import Television

def test_power():
    tv = Television()
    assert not tv._Television__status
    tv.power()
    assert tv._Television__status
    tv.power()
    assert not tv._Television__status

def test_mute():
    tv = Television()
    assert not tv._Television__status
    tv.power()
    tv.mute()
    assert tv._Television__muted
    tv.mute()
    assert not tv._Television__muted

def test_channel_up():
    tv = Television()
    assert not tv._Television__status
    tv.power()
    tv.channel_up()
    assert tv._Television__channel == 1

def test_channel_down():
    tv = Television()
    assert not tv._Television__status
    tv.power()
    tv.channel_down()
    assert tv._Television__channel == 3

def test_volume_up():
    tv = Television()
    assert not tv._Television__status
    tv.power()
    tv.volume_up()
    assert tv._Television__volume == 1

def test_volume_down():
    tv = Television()
    assert not tv._Television__status
    tv.power()
    for _ in range(Television.MAX_VOLUME):
        tv.volume_up()
    tv.volume_down()
    assert tv._Television__volume == 1

def test_str_unmuted():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

def test_str_muted():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = Muted"
