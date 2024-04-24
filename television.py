
class Television:
  MIN_VOLUME = 0
  MAX_VOLUME = 2
  MIN_CHANNEL = 0
  MAX_CHANNEL = 3

  def __init__(self):
    """Initialize the Television object with default values."""
    self.__status: bool = False
    self.__muted: bool = False
    self.__volume: int = self.MIN_VOLUME
    self.__channel: int = self.MIN_CHANNEL

  def power(self) -> None:
    """Turn the TV on or off."""
    self.__status = not self.__status

  def mute(self) -> None:
    """Mute or unmute the TV if it's on."""
    if self.__status:
      self.__muted = not self.__muted

  def channel_up(self) -> None:
    """Increase the TV channel if it's on."""
    if self.__status:
      self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)

  def channel_down(self) -> None:
    """Decrease the TV channel if it's on."""
    if self.__status:
      if self.__channel == Television.MIN_CHANNEL:
        self.__channel = Television.MAX_CHANNEL
      else:
        self.__channel -= 1

  def volume_up(self) -> None:
    """Increase the TV volume if it's on."""
    if self.__status:
      if self.__muted:
        self.__muted = False
      else:
        self.__volume = min(self.__volume + 1, Television.MAX_VOLUME)

  def volume_down(self) -> None:
    """Decrease the TV volume if it's on."""
    if self.__status:
      if self.__muted:
        self.__muted = False
      else:
        self.__volume = max(self.__volume - 1, Television.MIN_VOLUME)

  def __str__(self) -> str:
    """Return string representation of Television object."""
    if self.__muted:
      return f"Power = {self.__status}, Channel = {self.__channel}, Volume = Muted"
    else:
      return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
