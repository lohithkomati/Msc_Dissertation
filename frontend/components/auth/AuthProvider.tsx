"use client";

import {
    createContext,
    useContext,
    useEffect,
    useState,
    ReactNode,
} from "react";

import { api } from "@/lib/api";

export interface User {

    id: number;

    username: string;

    email: string;

    first_name: string;

    last_name: string;

    role: string;

}

interface AuthContextType {

    user: User | null;

    loading: boolean;

    login: (
        username: string,
        password: string
    ) => Promise<void>;

    logout: () => void;

    refreshProfile: () => Promise<void>;

}

const AuthContext = createContext<AuthContextType | null>(
    null
);

interface Props {

    children: ReactNode;

}

export function AuthProvider({

    children,

}: Props) {

    const [user, setUser] =
        useState<User | null>(null);

    const [loading, setLoading] =
        useState(true);

    useEffect(() => {

        const token =
            localStorage.getItem("access");

        if (token) {

            refreshProfile();

        }

        else {

            setLoading(false);

        }

    }, []);

    async function login(

        username: string,

        password: string

    ) {

        const result: any =
            await api.login({

                username,

                password,

            });

        localStorage.setItem(

            "access",

            result.access

        );

        localStorage.setItem(

            "refresh",

            result.refresh

        );

        await refreshProfile();

    }

    async function refreshProfile() {

        try {

            const profile: any =
                await api.profile();

            setUser(profile);

        }

        catch {

            localStorage.removeItem("access");

            localStorage.removeItem("refresh");

            setUser(null);

        }

        finally {

            setLoading(false);

        }

    }

    function logout() {

        localStorage.removeItem("access");

        localStorage.removeItem("refresh");

        setUser(null);

    }

    return (

        <AuthContext.Provider

            value={{

                user,

                loading,

                login,

                logout,

                refreshProfile,

            }}

        >

            {children}

        </AuthContext.Provider>

    );

}

export function useAuth() {

    const context =
        useContext(AuthContext);

    if (!context) {

        throw new Error(

            "useAuth must be used inside AuthProvider"

        );

    }

    return context;

}