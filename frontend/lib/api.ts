import {

    getAccessToken,

    getRefreshToken,

    saveTokens,

    clearTokens,

} from "./auth";

const API_BASE = process.env.NEXT_PUBLIC_API;

let refreshing = false;

let refreshPromise: Promise<boolean> | null = null;

async function refreshAccessToken(): Promise<boolean> {

    if (refreshing && refreshPromise) {

        return refreshPromise;

    }

    refreshing = true;

    refreshPromise = (async () => {

        try {

            const refresh = getRefreshToken();

            if (!refresh) {

                return false;

            }

            const response = await fetch(

                `${API_BASE}/users/refresh/`,

                {

                    method: "POST",

                    headers: {

                        "Content-Type": "application/json",

                    },

                    body: JSON.stringify({

                        refresh,

                    }),

                }

            );

            if (!response.ok) {

                return false;

            }

            const data = await response.json();

            saveTokens(

                data.access,

                refresh

            );

            return true;

        }

        catch {

            return false;

        }

        finally {

            refreshing = false;

            refreshPromise = null;

        }

    })();

    return refreshPromise;

}

async function request<T>(

    endpoint: string,

    options: RequestInit = {}

): Promise<T> {

    const headers: HeadersInit = {

        "Content-Type": "application/json",

        ...options.headers,

    };

    const token = getAccessToken();

    if (token) {

        headers["Authorization"] = `Bearer ${token}`;

    }

    let response = await fetch(

        `${API_BASE}${endpoint}`,

        {

            ...options,

            headers,

        }

    );

    if (response.status === 401) {

        const refreshed = await refreshAccessToken();

        if (refreshed) {

            const retryHeaders: HeadersInit = {

                "Content-Type": "application/json",

                ...options.headers,

                Authorization: `Bearer ${getAccessToken()}`,

            };

            response = await fetch(

                `${API_BASE}${endpoint}`,

                {

                    ...options,

                    headers: retryHeaders,

                }

            );

        }

        else {

            clearTokens();

            if (typeof window !== "undefined") {

                window.location.href = "/login";

            }

            throw new Error(

                "Session expired."

            );

        }

    }

    if (!response.ok) {

        let message = "Request failed.";

        try {

            const error = await response.json();

            message =

                error.detail ||

                JSON.stringify(error);

        }

        catch {}

        throw new Error(message);

    }

    return response.json();

}

export const api = {

    login(data: {

        username: string;

        password: string;

    }) {

        return request("/users/login/", {

            method: "POST",

            body: JSON.stringify(data),

        });

    },

    register(data: unknown) {

        return request("/users/register/", {

            method: "POST",

            body: JSON.stringify(data),

        });

    },

    profile() {

        return request("/users/profile/");

    },

    listCases() {

        return request("/cases/");

    },

    getCase(id: number) {

        return request(`/cases/${id}/`);

    },

    createSession(caseId: number) {

        return request("/sessions/", {

            method: "POST",

            body: JSON.stringify({

                case_id: caseId,

            }),

        });

    },

    sendMessage(

        sessionId: number,

        history: unknown[],

        message: string,

        caseData?: unknown

    ) {

        return request(

            `/sessions/${sessionId}/chat/`,

            {

                method: "POST",

                body: JSON.stringify({

                    message,

                    history,

                    case: caseData,

                }),

            }

        );

    },

    completeSession(

        sessionId: number

    ) {

        return request(

            `/sessions/${sessionId}/complete/`,

            {

                method: "POST",

            }

        );

    },

    history() {

        return request(

            "/sessions/history/"

        );

    },

    feedback(

        sessionId: number

    ) {

        return request(

            `/feedback/${sessionId}/`

        );

    },

    generateFeedback(

        sessionId: number

    ) {

        return request(

            `/feedback/${sessionId}/generate/`,

            {

                method: "POST",

            }

        );

    },

};
};