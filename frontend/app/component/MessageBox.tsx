
import Conversation from "./Conversation";
import ChatArea from "./ChatArea";

const MessageBox = () => {

    return (
        <>
            <div className="flex grow">
                <div className="flex flex-col w-full">
                    <div className="py-5 px-10">
                        NAVBAR HERE
                    </div>
                    <div className="flex h-dvh mx-50 relative">
                        <div className="flex-6">
                            <Conversation />
                        </div>
                        <div className="absolute w-full bottom-15 p-2 bg-white text-palette-dark rounded-2xl  ">
                            <ChatArea />
                        </div> 
                    </div>
                    
                </div>
            </div>
        </>);
}

export default MessageBox;