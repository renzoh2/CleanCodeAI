import type { Route } from "./+types/Blackboard";
import { useNavigate } from "react-router";

export function meta({}: Route.MetaArgs){
    return [
        {
            title: "Clean Code AI - Blackboard"
        },
        {
            name: "description",
            content: "The Blackboard for Clean Code AI",
        }
    ]
}

const Blackboard = () => {
    const navigate = useNavigate();

    return (
        <>
        Blackboard Page
        <button onClick={() => navigate('/')} >Go Back</button>
        </>
    )
}

export default Blackboard;