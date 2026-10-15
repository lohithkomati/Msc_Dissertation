"use client";

import { useState } from "react";

export default function VoiceInput() {

    const [

        recording,

        setRecording,

    ] = useState(false);

    async function toggleRecording() {

        if (!recording) {

            const stream = await navigator.mediaDevices.getUserMedia({

                audio: true,

            });

            console.log(stream);

            setRecording(true);

        }

        else {

            setRecording(false);

        }

    }

    return (

        <div className="space-y-4">

            <button

                onClick={toggleRecording}

                className={`

                w-full

                rounded-lg

                py-3

                font-semibold

                ${

                    recording

                        ? "bg-red-600"

                        : "bg-accent text-black"

                }

                `}

            >

                {

                    recording

                        ? "Stop Recording"

                        : "Start Recording"

                }

            </button>

            <p className="text-sm text-slate-400">

                Browser microphone input.

            </p>

        </div>

    );

}