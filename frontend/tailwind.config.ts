import type { Config } from "tailwindcss";

const config: Config = {

    content: [

        "./app/**/*.{ts,tsx}",

        "./components/**/*.{ts,tsx}",

        "./pages/**/*.{ts,tsx}",

    ],

    theme: {

        extend: {

            colors: {

                bg: {

                    deep: "#023E4F",

                    surface: "#04526A",

                    elevated: "#065E7A",

                },

                accent: "#02C39A",

                border: "#0A7A9A",

                success: "#10B981",

                warning: "#F59E0B",

                error: "#EF4444",

            },

        },

    },

    plugins: [],

};

export default config;