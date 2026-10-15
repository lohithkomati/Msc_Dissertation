from .rubric import OSCE_RUBRIC


def check_transcript(

    transcript: str,

):

    doctor = " ".join(

        line.lower()

        for line in transcript.splitlines()

        if line.startswith("Doctor:")

    )

    results = {}

    for domain in OSCE_RUBRIC["domains"]:

        results[domain["key"]] = True

    return results