"use client";

import { useEffect, useRef } from "react";

interface Props{

message:string;

type?:"status"|"alert";

}

export function LiveRegion({

message,

type="status",

}:Props){

const ref=useRef<HTMLDivElement>(null);

useEffect(()=>{

if(!ref.current)return;

ref.current.textContent="";

const timer=setTimeout(()=>{

if(ref.current){

ref.current.textContent=message;

}

},50);

return()=>clearTimeout(timer);

},[message]);

return(

<div

ref={ref}

role={type}

aria-live={

type==="alert"

?"assertive"

:"polite"

}

aria-atomic="true"

className="sr-only"

/>

);

}