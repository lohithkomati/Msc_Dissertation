import type { Metadata } from "next";
import { Inter } from "next/font/google";

import "../styles/globals.css";

import { AuthProvider } from "@/components/auth/AuthProvider";

const inter = Inter({
    subsets: ["latin"],
    display: "swap",
    variable: "--font-inter",
});

export const metadata: Metadata = {
    title: {
        default: "VAGUS AI",
        template: "%s | VAGUS AI",
    },
    description: "AI Clinical Consultation Simulator",
};

interface RootLayoutProps {
    children: React.ReactNode;
}

export default function RootLayout({
    children,
}: RootLayoutProps) {

    return (
        <html
            lang="en"
            className={inter.variable}
        >
            <body>

                <a
                    href="#main-content"
                    className="skip-link"
                >
                    Skip to main content
                </a>

                <AuthProvider>

                    {children}

                </AuthProvider>

            </body>
        </html>
    );
}