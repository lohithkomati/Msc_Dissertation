"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

import { api } from "@/lib/api";

export default function RegisterForm() {

    const router = useRouter();

    const [form, setForm] = useState({

        username: "",

        email: "",

        first_name: "",

        last_name: "",

        password: "",

        confirm_password: "",

    });

    const [loading, setLoading] = useState(false);

    const [error, setError] = useState("");

    function updateField(

        field: keyof typeof form,

        value: string

    ) {

        setForm({

            ...form,

            [field]: value,

        });

    }

    async function submit(

        e: React.FormEvent

    ) {

        e.preventDefault();

        setError("");

        if (

            form.password !==

            form.confirm_password

        ) {

            setError(

                "Passwords do not match."

            );

            return;

        }

        setLoading(true);

        try {

            await api.register({

                username: form.username,

                email: form.email,

                first_name: form.first_name,

                last_name: form.last_name,

                password: form.password,

            });

            router.push("/login");

        }

        catch (err: any) {

            setError(

                err.message ||

                "Registration failed."

            );

        }

        finally {

            setLoading(false);

        }

    }

    return (

        <form

            onSubmit={submit}

            className="w-full max-w-lg rounded-xl bg-bg-surface p-8"

        >

            <h1 className="mb-8 text-3xl font-bold text-white">

                Create Account

            </h1>

            {error && (

                <div className="mb-6 rounded bg-red-600 p-3 text-white">

                    {error}

                </div>

            )}

            <input

                className="mb-4 w-full rounded p-3 text-black"

                placeholder="Username"

                value={form.username}

                onChange={(e) =>

                    updateField(

                        "username",

                        e.target.value

                    )

                }

            />

            <input

                className="mb-4 w-full rounded p-3 text-black"

                placeholder="Email"

                type="email"

                value={form.email}

                onChange={(e) =>

                    updateField(

                        "email",

                        e.target.value

                    )

                }

            />

            <input

                className="mb-4 w-full rounded p-3 text-black"

                placeholder="First Name"

                value={form.first_name}

                onChange={(e) =>

                    updateField(

                        "first_name",

                        e.target.value

                    )

                }

            />

            <input

                className="mb-4 w-full rounded p-3 text-black"

                placeholder="Last Name"

                value={form.last_name}

                onChange={(e) =>

                    updateField(

                        "last_name",

                        e.target.value

                    )

                }

            />

            <input

                className="mb-4 w-full rounded p-3 text-black"

                placeholder="Password"

                type="password"

                value={form.password}

                onChange={(e) =>

                    updateField(

                        "password",

                        e.target.value

                    )

                }

            />

            <input

                className="mb-8 w-full rounded p-3 text-black"

                placeholder="Confirm Password"

                type="password"

                value={form.confirm_password}

                onChange={(e) =>

                    updateField(

                        "confirm_password",

                        e.target.value

                    )

                }

            />

            <button

                disabled={loading}

                className="w-full rounded bg-accent py-3 font-semibold text-black"

            >

                {

                    loading

                        ? "Creating Account..."

                        : "Register"

                }

            </button>

        </form>

    );

}