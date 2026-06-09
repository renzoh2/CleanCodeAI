import type { Route } from "./+types/Blackboard";
import { useNavigate } from "react-router";
import  SideBar from "../component/SideBar";
import ChatBox from "../component/ChatBox";

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
        <div className="flex flex-row h-screen w-screen">
            <SideBar />
            <ChatBox />
        </div>
       
        </>
    )
}

export default Blackboard;