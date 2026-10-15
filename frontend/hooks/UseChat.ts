"use client";

import { useState } from "react";

import { api } from "@/lib/api";

export interface ChatMessage {

    role: "user" | "assistant";

    content: string;

}

export function useChat(

    sessionId: number,

    caseData?: unknown

) {

    const [

        messages,

        setMessages,

    ] = useState<ChatMessage[]>([]);

    const [

        loading,

        setLoading,

    ] = useState(false);

    const [

        audio,

        setAudio,

    ] = useState("");

    async function send(

        message: string

    ) {

        if (!message.trim()) return;

        const history = [

            ...messages,

            {

                role: "user" as const,

                content: message,

            },

        ];

        setMessages(history);

        setLoading(true);

        try {

            const result: any =

                await api.sendMessage(

                    sessionId,

                    history,

                    message,

                    caseData

                );

            setMessages([

                ...history,

                {

                    role: "assistant",

                    content:

                        result.response,

                },

            ]);

            setAudio(

                result.audio_b64 || ""

            );

        }

        finally {

            setLoading(false);

        }

    }

    return {

        messages,

        loading,

        audio,

        send,

    };

}