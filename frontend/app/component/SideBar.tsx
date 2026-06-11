
import imgBubbleChat from "/img/bubble-chat.png";
import imgCode from "/img/code.png";
import imgNewMessage from "/img/new-message.png";

const SideBar = () => {

    

    return (
        <>
            <div>
                <div>
                    <a href="">
                        New Chat
                        <img src={imgNewMessage} />
                    </a>
                </div>
                <div>
                    <a href="">
                        Chats
                        <img src={imgBubbleChat} />
                    </a>
                </div>
                <div>
                    <a href="">
                        Connect to VSCode
                        <img src={imgCode} />
                    </a>
                </div>
            </div>
        </>
    )
}

export default SideBar;