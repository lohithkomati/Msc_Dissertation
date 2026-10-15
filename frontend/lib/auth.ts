export function getAccessToken(): string {

    if (typeof window === "undefined") {

        return "";

    }

    return localStorage.getItem("access") || "";

}

export function getRefreshToken(): string {

    if (typeof window === "undefined") {

        return "";

    }

    return localStorage.getItem("refresh") || "";

}

export function saveTokens(

    access: string,

    refresh: string

) {

    localStorage.setItem(

        "access",

        access

    );

    localStorage.setItem(

        "refresh",

        refresh

    );

}

export function clearTokens() {

    localStorage.removeItem(

        "access"

    );

    localStorage.removeItem(

        "refresh"

    );

}

export function isAuthenticated() {

    return !!getAccessToken();

}