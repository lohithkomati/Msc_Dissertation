interface Props{

feedback:any;

}

export default function FeedbackSummary({

feedback,

}:Props){

return(

<div className="space-y-8">

<section>

<h2 className="text-2xl font-semibold">

Narrative Feedback

</h2>

<p className="mt-4 whitespace-pre-wrap">

{feedback.narrative_feedback}

</p>

</section>

<section>

<h2 className="text-2xl font-semibold">

Diagnosis

</h2>

<p className="mt-4">

{

feedback.diagnosis_correct

?"Correct"

:"Incorrect"

}

</p>

<p>

{feedback.diagnosis_feedback}

</p>

</section>

<section>

<h2 className="text-2xl font-semibold">

Missed Questions

</h2>

<ul className="list-disc ml-8 mt-4">

{

feedback.missed_questions.map(

(q:string)=>(

<li key={q}>

{q}

</li>

)

)

}

</ul>

</section>

</div>

);

}