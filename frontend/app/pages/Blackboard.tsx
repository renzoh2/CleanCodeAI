import type { Route } from "./+types/Blackboard";
import { useNavigate } from "react-router";
import  SideBar from "../component/SideBar"

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
        <div>
            <SideBar/>
            <div>
                Blackboard Page
            </div>
        </div>
       
        </>
    )
}

export default Blackboard;