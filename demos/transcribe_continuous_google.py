import sys
from os.path import dirname
sys.path.append(dirname(__file__) + "/../")

# Very simple script which just prints ASR results to a screen as an ongoing chain.
# You have to be authenticated by Google Cloud (see modules/asr/)

from incrementaldialoguesystem.modules.asr import AutomaticSpeechRecogniser


if __name__ == "__main__":
    AutomaticSpeechRecogniser()
