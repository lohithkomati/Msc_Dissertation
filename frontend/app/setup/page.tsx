"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

interface PatientCase {
  id: number;
  title: string;
  patient_name: string;
  condition: string;
  specialty: string;
  difficulty: string;
}

export default function SetupPage() {
  const router = useRouter();

  const [cases, setCases] = useState<PatientCase[]>([]);
  const [selectedCase, setSelectedCase] = useState<number>();
  const [loading, setLoading] = useState(true);
  const [starting, setStarting] = useState(false);

  useEffect(() => {
    loadCases();
  }, []);

  async function loadCases() {
    try {
      const res = await fetch(
        `${process.env.NEXT_PUBLIC_API}/cases/`
      );

      const data = await res.json();

      setCases(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

  async function startConsultation() {
    if (!selectedCase) return;

    setStarting(true);

    const token = localStorage.getItem("access");

    const response = await fetch(
      `${process.env.NEXT_PUBLIC_API}/sessions/`,
      {
        method: "POST",

        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },

        body: JSON.stringify({
          case_id: selectedCase,
        }),
      }
    );

    const session = await response.json();

    router.push(`/consult/${session.id}`);
  }

  if (loading) {
    return (
      <main className="min-h-screen flex justify-center items-center text-white">
        Loading patient cases...
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-bg-deep text-white p-10">

      <h1 className="text-4xl font-bold mb-10">

        Select Clinical Scenario

      </h1>

      <div className="grid gap-6">

        {cases.map((item) => (

          <button

            key={item.id}

            onClick={() => setSelectedCase(item.id)}

            className={`rounded-xl border p-6 text-left transition

            ${
              selectedCase === item.id
                ? "border-accent bg-bg-elevated"
                : "border-slate-700"
            }`}

          >

            <h2 className="text-2xl font-semibold">

              {item.title}

            </h2>

            <p>

              Patient

              {" : "}

              {item.patient_name}

            </p>

            <p>

              Condition

              {" : "}

              {item.condition}

            </p>

            <p>

              Specialty

              {" : "}

              {item.specialty}

            </p>

            <p>

              Difficulty

              {" : "}

              {item.difficulty}

            </p>

          </button>

        ))}

      </div>

      <button

        disabled={!selectedCase || starting}

        onClick={startConsultation}

        className="mt-10 px-8 py-4 rounded-xl bg-accent text-black font-bold disabled:opacity-40"

      >

        {starting

          ? "Creating Session..."

          : "Start Consultation"}

      </button>

    </main>
  );
}