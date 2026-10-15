import Link from "next/link";

export default function HomePage() {

    return (

        <main

            id="main-content"

            className="min-h-screen flex items-center justify-center bg-bg-deep"

        >

            <section

                className="max-w-4xl text-center px-8"

            >

                <h1

                    className="text-6xl font-bold text-white"

                >

                    VAGUS AI

                </h1>

                <p

                    className="mt-6 text-xl text-slate-200"

                >

                    Practice realistic medical consultations with AI patients.

                </p>

                <div

                    className="mt-12"

                >

                    <Link

                        href="/setup"

                        className="px-8 py-4 rounded-lg bg-accent text-black font-semibold"

                    >

                        Start Consultation

                    </Link>

                </div>

            </section>

        </main>

    );

}