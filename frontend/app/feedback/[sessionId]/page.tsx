"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";

import { api } from "@/lib/api";

import ScoreCard from "@/components/feedback/ScoreCard";
import DomainChart from "@/components/feedback/DomainChart";
import FeedbackSummary from "@/components/feedback/FeedbackSummary";

interface Feedback {

    overall_score:number;

    domain_scores:Record<string,number>;

    missed_questions:string[];

    diagnosis_correct:boolean;

    diagnosis_feedback:string;

    narrative_feedback:string;

}

export default function FeedbackPage(){

    const params=useParams();

    const sessionId=Number(params.sessionId);

    const [feedback,setFeedback]=useState<Feedback>();

    const [loading,setLoading]=useState(true);

    useEffect(()=>{

        load();

    },[]);

    async function load(){

        try{

            const data:any=await api.feedback(sessionId);

            setFeedback(data);

        }

        finally{

            setLoading(false);

        }

    }

    if(loading){

        return(

            <main className="flex min-h-screen items-center justify-center">

                Loading feedback...

            </main>

        );

    }

    if(!feedback){

        return(

            <main className="flex min-h-screen items-center justify-center">

                No feedback found.

            </main>

        );

    }

    return(

        <main className="min-h-screen bg-bg-deep text-white p-8">

            <h1 className="text-4xl font-bold mb-8">

                Consultation Feedback

            </h1>

            <ScoreCard

                score={feedback.overall_score}

            />

            <div className="mt-10">

                <DomainChart

                    scores={feedback.domain_scores}

                />

            </div>

            <div className="mt-10">

                <FeedbackSummary

                    feedback={feedback}

                />

            </div>

        </main>

    );

}