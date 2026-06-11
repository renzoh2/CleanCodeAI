
import Conversation from "./Conversation";
import ChatArea from "./ChatArea";
import NavBar from "./NavBar";

const MessageBox = () => {
    return (
        <>
            <div className="flex grow">
                <div className="flex flex-col w-full">
                    <div className="py-5 px-10">
                        <NavBar />
                    </div>
                    <div className="flex h-screen mx-40 relative overflow-hidden">
                        <div className="flex-6 overflow-y-auto scroll-smooth mb-20 p-5">
                            <Conversation />
                        </div>
                        <div className="absolute w-full bottom-5 p-2 bg-palette-white text-palette-dark rounded-2xl  ">
                            <ChatArea />
                        </div> 
                    </div>
                    
                </div>
            </div>
        </>);
}

export default MessageBox;