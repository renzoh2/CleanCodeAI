import useChatStore from "~/stores/useChatStore";
import ChatBalloon from "./ChatBalloon";
import { useState, useEffect, useRef } from "react";

enum ChatRoleEnums {
    SYSTEM = "SYSTEM",
    USER = "USER"
}

const Conversation = () => {

    const chat = useChatStore();
    const latestDivRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        setTimeout(() => {
            latestDivRef.current?.scrollIntoView({ behavior: 'smooth' });
        }, 0);

    }, [chat.contents])

    const lastAssistantIndex = chat.contents.reduce<number>(
        (acc, item, index) => item.role === ChatRoleEnums.USER? index : acc, -1
    );

    return (
        <>
            <div className="flex flex-col gap-5 scroll-smooth">
                
                {
                    chat.contents.map((item, index) => {

                        const style = item.role === ChatRoleEnums.USER
                            ? "bg-palette-gray max-w-3/6 text-wrap wrap-anywhere text-palette-white rounded-lg p-2 self-end"
                            : "text-palette-white text-wrap wrap-anywhere rounded-lg p-2 w-full";


                        return  <div key={index} className={style}>
                                    {index === lastAssistantIndex && <div ref={latestDivRef} />}
                                    <ChatBalloon message={item.content} role={item.role}/>
                                </div>
                    })
                }
                
                
            </div>
        </>
    );
}

export default Conversation