"use client";

import {

BarChart,

Bar,

XAxis,

YAxis,

Tooltip,

ResponsiveContainer,

} from "recharts";

interface Props{

scores:Record<string,number>;

}

export default function DomainChart({

scores,

}:Props){

const data=Object.entries(scores).map(

([key,value])=>({

name:key,

score:value,

})

);

return(

<div className="h-96 bg-bg-surface rounded-xl p-6">

<h2 className="text-2xl mb-4">

Domain Scores

</h2>

<ResponsiveContainer>

<BarChart

data={data}

>

<XAxis dataKey="name"/>

<YAxis domain={[0,10]}/>

<Tooltip/>

<Bar dataKey="score"/>

</BarChart>

</ResponsiveContainer>

</div>

);

}