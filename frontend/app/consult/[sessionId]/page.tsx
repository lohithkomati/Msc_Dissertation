"use client";

import { useState } from "react";

import MessageBubble from "./MessageBubble";

interface ChatMessage {

  role: "user" | "assistant";

  content: string;

}

interface Props {

  sessionId: number;

}

export default function ChatBox({

  sessionId,

}: Props) {

  const [messages, setMessages] = useState<ChatMessage[]>([]);

  const [input, setInput] = useState("");

  const [loading, setLoading] = useState(false);

  async function send() {

    if (!input.trim()) return;

    const token = localStorage.getItem("access");

    const updated = [

      ...messages,

      {

        role: "user",

        content: input,

      },

    ];

    setMessages(updated);

    setLoading(true);

    const response = await fetch(

      `${process.env.NEXT_PUBLIC_API}/sessions/${sessionId}/chat/`,

      {

        method: "POST",

        headers: {

          Authorization: `Bearer ${token}`,

          "Content-Type": "application/json",

        },

        body: JSON.stringify({

          message: input,

          history: updated,

        }),

      }

    );

    const data = await response.json();

    setMessages([

      ...updated,

      {

        role: "assistant",

        content: data.response,

      },

    ]);

    setInput("");

    setLoading(false);

  }

  return (

    <div className="flex flex-col h-full">

      <div className="flex-1 overflow-y-auto">

        {messages.map((m, index) => (

          <MessageBubble

            key={index}

            role={m.role}

            message={m.content}

          />

        ))}

      </div>

      <div className="flex gap-2 mt-4">

        <input

          className="flex-1 rounded-lg text-black px-4"

          value={input}

          onChange={(e) =>

            setInput(e.target.value)

          }

          placeholder="Ask the patient..."

        />

        <button

          onClick={send}

          disabled={loading}

          className="bg-accent text-black rounded-lg px-6"

        >

          Send

        </button>

      </div>

    </div>

  );

}