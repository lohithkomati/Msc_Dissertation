"use client";

import { useState } from "react";

import { useRouter } from "next/navigation";

import {

useAuth,

} from "./AuthProvider";

export default function LoginForm(){

const router=useRouter();

const{

login,

}=useAuth();

const[username,setUsername]=useState("");

const[password,setPassword]=useState("");

const[error,setError]=useState("");

const[loading,setLoading]=useState(false);

async function submit(e:React.FormEvent){

e.preventDefault();

setError("");

setLoading(true);

try{

await login(

username,

password

);

router.push("/setup");

}

catch{

setError(

"Invalid username or password."

);

}

finally{

setLoading(false);

}

}

return(

<form

onSubmit={submit}

className="w-full max-w-md rounded-xl bg-bg-surface p-8"

>

<h1 className="mb-8 text-3xl font-bold text-white">

Login

</h1>

{error&&(

<div className="mb-4 rounded bg-red-600 p-3 text-white">

{error}

</div>

)}

<input

className="mb-4 w-full rounded p-3 text-black"

placeholder="Username"

value={username}

onChange={(e)=>setUsername(e.target.value)}

/>

<input

type="password"

className="mb-6 w-full rounded p-3 text-black"

placeholder="Password"

value={password}

onChange={(e)=>setPassword(e.target.value)}

/>

<button

disabled={loading}

className="w-full rounded bg-accent py-3 font-semibold text-black"

>

{

loading

?

"Signing In..."

:

"Login"

}

</button>

</form>

);

}