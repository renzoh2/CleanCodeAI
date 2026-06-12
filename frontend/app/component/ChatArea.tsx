import { useState, useEffect, type ChangeEvent, type KeyboardEvent} from "react";

import ButtonSend from "/img/send.png";
import ButtonSendHover from "/img/send-hover.png";
import useChatStore from "../stores/useChatStore";

const greeting = [
    "Ask Anything",
    "How can I help you?"
];

const ChatArea = () => {
    
    const [chatmessage, setChatMessage] = useState<string>("");
    const [isHover, setIsHover] = useState(false);

    const [greetingMessage, setGreetingMessage] = useState<string>(greeting[0]);

    useEffect(() => {
        setGreetingMessage(greeting[Math.floor(Math.random() * greeting.length)]);
    }, []);

    const chat = useChatStore();

    const submitMessage = () => {
        if (!chatmessage.trim()) return;
        chat.addContent({
            role: "USER",
            content: [
                {
                    iteration: 0,
                    llm: undefined,
                    text: chatmessage.trim()
                }
            ]
        });
        chat.addContent({
            role: "SYSTEM",
            content: [
                {
                    iteration: 0,
                    llm: {
                        model: "GG",
                        temperature: 0.2
                    },
                    text: "TESTING"
                }
            ]
        });
        setChatMessage("");
    };

    const handleKeyDown = (e: KeyboardEvent<HTMLTextAreaElement>) => {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            submitMessage();
        }
    };

    return (<>
        <div className="flex">
            <textarea
                name="chatMessage"
                value={chatmessage}
                className="grow field-sizing-content resize-none max-h-[5lh] w-full outline-0 p-2"
                onChange={(e:ChangeEvent<HTMLTextAreaElement>) => {setChatMessage(e.target.value)}}
                onKeyDown={handleKeyDown}
                placeholder={greetingMessage}
            />
            <button 
                className="pr-2 h-10 self-end" 
                onMouseEnter={()=>{setIsHover(true)}} 
                onMouseLeave={()=>{setIsHover(false)}}
                onClick={submitMessage}
            >
                <img src={isHover ? ButtonSendHover : ButtonSend} className="w-7" alt="Send" />
            </button>
        </div>
    </>);
}

export default ChatArea;