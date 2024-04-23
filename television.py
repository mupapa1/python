class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """Initialize the Television object with default values."""
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self):
        """Turn the TV on or off."""
        self.__status = not self.__status

    def mute(self):
        """Mute or unmute the TV."""
        self.__muted = not self.__muted

    def channel_up(self):
        """Increase the TV channel."""
        if self.__status:
            self.__channel = (self.__channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self):
        """Decrease the TV channel."""
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        """Increase the TV volume."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__volume = min(self.__volume + 1, self.MAX_VOLUME)

    def volume_down(self):
        """Decrease the TV volume."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__volume = max(self.__volume - 1, self.MIN_VOLUME)

    def __str__(self):
        """Return string representation of Television object."""
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
