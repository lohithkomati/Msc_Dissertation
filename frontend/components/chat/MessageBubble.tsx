interface Props {

  role: "user" | "assistant";

  message: string;

}

export default function MessageBubble({

  role,

  message,

}: Props) {

  const isDoctor = role === "user";

  return (

    <div

      className={`flex

      ${

        isDoctor

          ? "justify-end"

          : "justify-start"

      }

      mb-4`}

    >

      <div

        className={`max-w-[70%]

        rounded-xl

        p-4

        ${

          isDoctor

            ? "bg-accent text-black"

            : "bg-bg-surface text-white"

        }`}

      >

        {message}

      </div>

    </div>

  );

}