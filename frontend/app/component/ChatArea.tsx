import { useState, useRef, useEffect, type ChangeEvent, type MouseEvent} from "react";

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
    const [mounted, setMounted] = useState(false);

    const [greetingMessage, setGreetingMessage] = useState<string>(greeting[0]);

    useEffect(() => {
        setGreetingMessage(greeting[Math.floor(Math.random() * greeting.length)]);
    }, []);

    useEffect(() => {
        setMounted(true);
    }, []);

    const chat = useChatStore();

    const textAreaRef = useRef<HTMLTextAreaElement>(null);


    const textAreaChange = (e: ChangeEvent<HTMLTextAreaElement>) => {
        setChatMessage(e.target.value);
    }

    const handleOperation = (e: MouseEvent<HTMLButtonElement>) => {
        e.preventDefault();
        chat.addMessage(chatmessage);
        setChatMessage('');
        if(textAreaRef.current){
            textAreaRef.current.value = "";
        }
    }

    return (<>
        <div className="flex">
            <textarea
                name="chatMessage"
                ref={textAreaRef}
                className="grow field-sizing-content resize-none max-h-[5lh] outline-0 p-2"
                onChange={textAreaChange}
                placeholder={greetingMessage}
            />
            <button 
                className="pr-2 h-10 self-end" 
                onMouseEnter={()=>{setIsHover(true)}} 
                onMouseLeave={()=>{setIsHover(false)}}
                onClick={handleOperation}
            >
                {mounted && (
                    <img src={isHover ? ButtonSendHover : ButtonSend} className="w-7" />
                )}
            </button>
        </div>
    </>);
}

export default ChatArea;