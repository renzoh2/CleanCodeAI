import { useState, useEffect } from "react";

interface MessageIterationInterface {
    iteration: number;
    text: string;
}

interface ChatBalloonInterface {
    role: string;
    message: MessageIterationInterface[];
}

enum ChatRoleEnums {
    SYSTEM = "SYSTEM",
    USER = "USER"
}

const ChatBalloon = (data: ChatBalloonInterface) => {
    const [styleSwitch, setStyleSwitch] = useState<string>();
    const [messageNumber, setMessageNumber] = useState<number>(0);
    const [message, setMessage] = useState<string>("");

    useEffect(() => {
        //Default Style
        setStyleSwitch("text-palette-white text-wrap wrap-anywhere rounded-lg p-2 w-full")

        if(data.role === ChatRoleEnums.USER){
            setStyleSwitch("bg-palette-gray max-w-3/6 text-wrap wrap-anywhere text-palette-white rounded-lg p-2 self-end")
        }

        setMessage(data.message[messageNumber].text)
    }, [])

    return (
        <>
            <div className={styleSwitch}>
                <div>
                    {message}
                </div>
                <div>
                    <div>
                        <button>regen ICON</button>
                    </div>
                    <div>
                        <button>Prev ICON</button>
                        <button>Next ICON</button>
                    </div>
                </div>
            </div>
        </>
    )
}

export default ChatBalloon;