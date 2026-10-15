import os
import tempfile

from faster_whisper import WhisperModel

_model = None


def get_whisper():

    global _model

    if _model is None:

        _model = WhisperModel(

            "medium",

            device="cpu",

            compute_type="int8",

        )

    return _model


def transcribe(audio_bytes: bytes) -> str:

    model = get_whisper()

    with tempfile.NamedTemporaryFile(

        suffix=".wav",

        delete=False,

    ) as tmp:

        tmp.write(audio_bytes)

        filename = tmp.name

    try:

        segments, _ = model.transcribe(

            filename,

            beam_size=5,

        )

        return " ".join(

            s.text.strip()

            for s in segments

        )

    finally:

        os.unlink(filename)