import os
import librosa
import numpy as np
import soundfile as sf
from datetime import datetime


# defining the class
class MusicTools:
    """This class contains bpm finder, key finder and vocal remover tools"""

    # initialize the class
    def __init__(self, filepath=None):

        self.filepath = filepath
        self.sr = None
        self.y = None
        self.keys = ["C", "C#", "D", "D#", "E", "E#", "F", "F#", "G", "G#", "A", "A#", "B"]

        # run load file function automatically
        self.load_file()

    # load the music file
    def load_file(self):
        """this method load the file and returns y,sr values"""
        try:
            if self.filepath is not None:
                audio_file = librosa.load(self.filepath, sr=None)
                y, sr = audio_file

                # change the y, sr values
                self.y, self.sr = y, sr
            else:
                return False

        except:
            return False

    # find the bpm
    def bpm_detector(self) -> str:
        """this method find the bpm and returns itt as a string"""
        tempo, beat_track = librosa.beat.beat_track(y=self.y, sr=self.sr)

        return "{:.2f}".format(tempo)

    # find the key
    def key_finder(self) -> str:
        """This method calculates the chromatogram and finds the key of song"""
        chromotogram = librosa.feature.chroma_stft(y=self.y, sr=self.sr)

        mean_chroma = np.mean(chromotogram, axis=1)

        return self.keys[np.argmax(mean_chroma)]

    # vocal-beat extractor
    def vocal_beat_extractor(self):
        """Separate vocal and beat."""
        try:
            location = os.path.expanduser("~/Desktop/")
            y_harmonic, y_percussion = librosa.effects.hpss(y=self.y)

            # Check if the desktop location exists
            if os.path.exists(location):
                sf.write(os.path.join(location, f"harmonic.wav"), y_harmonic, self.sr)
                sf.write(os.path.join(location, f"percussion.wav"), y_percussion, self.sr)
            else:
                print("Desktop location does not exist. Files not written.")
        except Exception as e:
            print(f"Error extracting vocal and beat: {e}")

