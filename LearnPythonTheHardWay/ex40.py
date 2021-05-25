class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def singmeasong(self):
        for line in self.lyrics:
            print(line)

happybday = Song(["Happy birthday to you",
                "I dont want to get sued",
                "So I'll stop right there"])

bullsonparade = Song(["They rally arround tha family",
                    "With pockets full of shells"])

happybday.singmeasong()

bullsonparade.singmeasong()