import base64
import os
import tempfile

import soundfile as sf

_engine = None


def get_tts():

    global _engine

    if _engine is not None:

        return _engine

    try:

        from kokoro_onnx import Kokoro

        _engine = Kokoro(

            "kokoro-v0_19.onnx",

            "voices.bin",

        )

    except Exception:

        _engine = None

    return _engine


def synthesise(

    text: str,

    voice: str = "af_sarah",

):

    engine = get_tts()

    if engine is None:

        return ""

    samples, sr = engine.create(

        text,

        voice=voice,

        speed=1.0,

        lang="en-us",

    )

    tmp = tempfile.NamedTemporaryFile(

        suffix=".wav",

        delete=False,

    )

    sf.write(

        tmp.name,

        samples,

        sr,

    )

    try:

        with open(

            tmp.name,

            "rb",

        ) as f:

            return base64.b64encode(

                f.read()

            ).decode()

    finally:

        os.unlink(tmp.name)