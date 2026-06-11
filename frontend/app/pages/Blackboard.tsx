import type { Route } from "./+types/Blackboard";
import { useNavigate } from "react-router";
import  SideBar from "../component/SideBar";
import MessageBox from "../component/MessageBox";

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
            <MessageBox />
        </div>
        </>
    );
}

export default Blackboard;