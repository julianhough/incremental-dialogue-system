# incremental-dialogue-system

## Python streaming demo

The python demo is modified from:

[https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/speech/microphone/transcribe_streaming_infinite.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/speech/microphone/transcribe_streaming_infinite.py```)

* To run the Python demo file `python/transcribe_streaming_infinite.py` you will need to be authenticated by Google Cloud appropriately so that you can use the Speech API, likely using an api key which will be stored locally. Note that you get 60 minutes a month of audio processing free before being charged.

* You need to make sure [PortAudio](https://www.portaudio.com/) is installed on your machine and that you have microphone access to the terminal application you run the python file from (you can use the command "brew install portaudio" in mac OS systems to achieve this).

* Ensure `pip` is installed and install the Python requirements, by running from the `python` subfolder `pip install -r requirements.txt`

* Run the demo from the `demo` subfolder simply with ```python transcribe_streaming_infinite.py```

You should start seeing the words stream to the screen in red when they are hypothesized, then green when finalized. Try to see how the word hypotheses are updating (both in terms of the word and the timing) in real-time and test it out (try to break catch it out).

In terms of Natural Language Understanding, currently due to the `if` statement starting at line 298 `if re.search(r"\b(exit|quit)\b", transcript, re.I):` the system only responds to the words "exit" or "quit", which both stop the stream. You can modify the function `generate_speech_contribution_from_input` to make a simple chatbot which responds to speech appropriately. For mac users, code is already there to respond to some keywords if you set `mac_system` to True. Be wary that if you use a Text-to-Speech like the `say` command in Mac, the speech API will recognise those words unless you have a headset ensuring no bleed into your microphone.
