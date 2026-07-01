//import { useNavigate } from "react-router";
import  SideBar from "~/component/SideBar";
import MessageBox from "~/component/MessageBox";


const Blackboard = () => {
    //const navigate = useNavigate();

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