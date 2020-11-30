from currentPet import Emotion
from Petfuture import future
class state:

    def __init__(self, name):
        self.current = {
                              '✔ Name':name, '✔ Level':1,
                              '･ᴗ･  happy': 30, '⌣_⌣́    tired': 20, 'ʘ‿ʘ  dirty': 20, '°⌓° hungry': 20
                              }

    def displayCurrent(self):
        petEmotion = ""
        for state, percentage in self.current.items():
            word = "{} : {}".format(state, percentage)
            if state == '･ᴗ･  happy':
                petEmotion += '\n'
                petEmotion += word
                petEmotion += '\n'
            else:
                petEmotion += word
                petEmotion += '\n'

        return petEmotion


    def currentShape(self):
        if self.current['･ᴗ･  happy'] <= 0:
            return Emotion[5]
        elif self.current['⌣_⌣́    tired']>=60:
            return Emotion[2]
        elif self.current['°⌓° hungry']>=60:
            return Emotion[4]
        elif self.current['ʘ‿ʘ  dirty']>=60:
            return Emotion[3]
        elif self.current['･ᴗ･  happy'] >= 60:
            return Emotion[1]
        else:
            return Emotion[0]

    def futureShape(self, job):
        if job == 'doctor':
            return future[0]
        elif job == 'soccer player':
            return future[1]
        elif job == "president":
            return future[2]
        else:
            return future[3]




