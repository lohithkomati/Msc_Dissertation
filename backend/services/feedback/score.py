import asyncio
import json
import re

from services.llm import llm_complete

from .checker import check_transcript
from .rubric import OSCE_RUBRIC


STAGE_1_PROMPT = """
You are a senior OSCE examiner.

PATIENT CASE

{patient_story}

TRANSCRIPT

{transcript}

RULE CHECKS

{keyword_results}

Return ONLY JSON.

{
  "domain_scores":{
      "presenting_complaint":0,
      "history_of_pc":0,
      "past_medical_history":0,
      "drug_history":0,
      "family_history":0,
      "social_history":0,
      "ice":0,
      "systems_review":0,
      "summarising":0,
      "communication":0
  },

  "missed_questions":[],

  "diagnosis_correct":false,

  "diagnosis_feedback":""
}
"""


STAGE_2_PROMPT = """
You are a supportive medical educator.

Domain scores

{scores}

Missed questions

{missed}

Diagnosis correct

{diagnosis_correct}

Write supportive constructive feedback.

Three to five sentences.

Plain text only.
"""


def extract_json(text):

    try:

        return json.loads(text)

    except Exception:

        pass

    match = re.search(

        r"\{.*\}",

        text,

        re.DOTALL,

    )

    if match:

        try:

            return json.loads(

                match.group()

            )

        except Exception:

            pass

    return {}


async def score_once(

    patient_story,

    transcript,

    keyword_summary,

    temperature,

):

    response = await llm_complete(

        messages=[

            {

                "role": "user",

                "content": STAGE_1_PROMPT.format(

                    patient_story=patient_story,

                    transcript=transcript,

                    keyword_results=keyword_summary,

                ),

            }

        ],

        system_prompt=(

            "Reply only using valid JSON."

        ),

        temperature=temperature,

        max_tokens=800,

    )

    return extract_json(response)


async def generate_feedback(session):

    transcript = "\n".join(

        [

            (

                "Doctor"

                if m["role"] == "user"

                else "Patient"

            )

            + ": "

            + m["content"]

            for m in session.messages

        ]

    )

    keyword_results = check_transcript(

        transcript

    )

    keyword_summary = "\n".join(

        [

            f"{k}: {v}"

            for k, v in keyword_results.items()

        ]

    )

    first, second = await asyncio.gather(

        score_once(

            session.case.patient_story,

            transcript,

            keyword_summary,

            0.15,

        ),

        score_once(

            session.case.patient_story,

            transcript,

            keyword_summary,

            0.35,

        ),

    )

    scores = {}

    for domain in OSCE_RUBRIC["domains"]:

        key = domain["key"]

        s1 = (

            first.get(

                "domain_scores",

                {},

            ).get(

                key,

                0,

            )

        )

        s2 = (

            second.get(

                "domain_scores",

                {},

            ).get(

                key,

                0,

            )

        )

        scores[key] = round(

            (

                s1

                + s2

            )

            / 2

        )

    overall = round(

        sum(

            scores.values()

        )

        / len(scores)

        * 10

    )

    missed = first.get(

        "missed_questions",

        [],

    )

    diagnosis_correct = first.get(

        "diagnosis_correct",

        False,

    )

    diagnosis_feedback = first.get(

        "diagnosis_feedback",

        "",

    )

    score_text = "\n".join(

        [

            f"{k}: {v}/10"

            for k, v in scores.items()

        ]

    )

    narrative = await llm_complete(

        messages=[

            {

                "role": "user",

                "content": STAGE_2_PROMPT.format(

                    scores=score_text,

                    missed=", ".join(missed),

                    diagnosis_correct=diagnosis_correct,

                ),

            }

        ],

        system_prompt=(

            "You are an experienced medical educator."

        ),

        temperature=0.6,

        max_tokens=350,

    )

    return {

        "overall_score": overall,

        "domain_scores": scores,

        "missed_questions": missed,

        "diagnosis_correct": diagnosis_correct,

        "diagnosis_feedback": diagnosis_feedback,

        "narrative_feedback": narrative,

        "keyword_checks": keyword_results,

    }