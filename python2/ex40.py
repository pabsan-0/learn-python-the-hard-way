
class Song(object):         # self and object are reserved words
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self,ergo):
        for line in self.lyrics:
            print line
        print ergo

# instance of the class Song
happy_bday = Song(['Happy birthday to you',
                   'I don\'t wanna get sued',
                   'So I\'ll stop right here'])


bulls_on_parade = Song(['They rally around the family',
                        'with a pocket full of shells'])

happy_bday.sing_me_a_song(1)

bulls_on_parade.sing_me_a_song('weon')
