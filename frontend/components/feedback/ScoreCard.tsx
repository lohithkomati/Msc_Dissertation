interface Props{

    score:number;

}

export default function ScoreCard({

    score,

}:Props){

    const colour=

        score>=80

        ?"bg-green-600"

        :score>=60

        ?"bg-yellow-500"

        :"bg-red-600";

    return(

        <div className={`${colour} rounded-xl p-8`}>

            <h2 className="text-2xl font-semibold">

                Overall Score

            </h2>

            <p className="text-6xl font-bold mt-4">

                {score}%

            </p>

        </div>

    );

}