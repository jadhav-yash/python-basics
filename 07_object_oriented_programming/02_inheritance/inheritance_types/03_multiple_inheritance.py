# One Child class inherits from Multiple Parent classes.

# ==========================================
# MULTIPLE INHERITANCE
# ==========================================

class Camera:

    def click_photo(self):

        print("Photo Clicked")


class MusicPlayer:

    def play_music(self):

        print("Music Playing")


# Child inherits from two classes
class SmartPhone(Camera, MusicPlayer):

    pass


phone = SmartPhone()

phone.click_photo()

phone.play_music()