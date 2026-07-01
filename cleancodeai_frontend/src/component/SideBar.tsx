
import imgBubbleChat from "/img/bubble-chat.png";
import imgCode from "/img/code.png";
import imgNewMessage from "/img/new-message.png";
import useChatStore from "~/stores/useChatStore";

const SideBar = () => {

    const chatStore = useChatStore();
    
    const newChat = () => {
        chatStore.restartContent();
    }
    
    return (
        <>
            <div className="flex flex-col w-1/6">
                <ul className="flex-col grow">
                    <li className="hover:bg-palette-gray my-2 hover:text-palette-white hover:rounded-xl active:bg-palette-red active:text-palette-white">
                        <a onClick={newChat} className="flex flex-row px-5 py-3  gap-2">
                            <img src={imgNewMessage} className="invert w-5" />
                            <span className="text-sm">New Chat</span>
                        </a>
                    </li>
                    <li className="hover:bg-palette-gray my-2 hover:text-palette-white hover:rounded-xl active:bg-palette-red active:text-palette-white">
                        <a href="" className="flex flex-row px-5 py-3  gap-2">
                            <img src={imgBubbleChat} className="invert w-5" />
                            <span className="text-sm">Chats</span>
                        </a>
                    </li>
                    <li className="hover:bg-palette-gray my-2 hover:text-palette-white hover:rounded-xl active:bg-palette-red active:text-palette-white">
                        <a href="" className="flex flex-row px-5 py-3  gap-2">
                            <img src={imgCode} className="invert w-5" />
                            <span className="text-sm">Connect to VSCode</span>
                        </a>
                    </li>
                </ul>
                
                <div className="p-5">
                    PROFILE
                </div>
            </div>
        </>
    )
}

export default SideBar;