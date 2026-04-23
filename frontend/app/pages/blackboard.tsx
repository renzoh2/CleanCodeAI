import type { Route } from "./+types/blackboard";

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
    return (
        <>Blackboard Page</>
    )
}

export default Blackboard;