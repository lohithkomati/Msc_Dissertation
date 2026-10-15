"use client";

import { useState } from "react";

import MessageBubble from "./MessageBubble";
import AudioPlayer from "@/components/voice/AudioPlayer";
import { useChat } from "@/hooks/useChat";

interface Props {
    sessionId: number;
}

export default function ChatBox({
    sessionId,
}: Props) {

    const [input, setInput] = useState("");

    const {

        messages,

        loading,

        audio,

        send,

    } = useChat(sessionId);

    async function handleSend() {

        if (!input.trim()) return;

        await send(input);

        setInput("");

    }

    function handleKeyDown(
        event: React.KeyboardEvent<HTMLInputElement>
    ) {

        if (event.key === "Enter") {

            handleSend();

        }

    }

    return (

        <div className="flex flex-col h-full">

            {/* Chat Messages */}

            <div className="flex-1 overflow-y-auto space-y-4 p-4">

                {messages.length === 0 && (

                    <div className="text-center text-slate-400 mt-12">

                        Start the consultation by asking the patient a question.

                    </div>

                )}

                {messages.map((message, index) => (

                    <MessageBubble
                        key={index}
                        role={message.role}
                        message={message.content}
                    />

                ))}

                {loading && (

                    <div className="text-slate-400 italic">

                        Patient is typing...

                    </div>

                )}

            </div>

            {/* Automatically play AI speech */}

            <AudioPlayer audio={audio} />

            {/* Input Area */}

            <div className="border-t border-slate-700 p-4">

                <div className="flex gap-3">

                    <input

                        type="text"

                        value={input}

                        disabled={loading}

                        placeholder="Ask the patient a question..."

                        onChange={(e) =>

                            setInput(e.target.value)

                        }

                        onKeyDown={handleKeyDown}

                        className="flex-1 rounded-lg border border-slate-600 bg-white px-4 py-3 text-black focus:border-cyan-500 focus:outline-none"

                    />

                    <button

                        onClick={handleSend}

                        disabled={loading || input.trim() === ""}

                        className="rounded-lg bg-accent px-8 py-3 font-semibold text-black transition hover:opacity-90 disabled:cursor-not-allowed disabled:opacity-50"

                    >

                        {

                            loading

                                ? "Sending..."

                                : "Send"

                        }

                    </button>

                </div>

            </div>

        </div>

    );

}