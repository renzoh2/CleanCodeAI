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
    const [messageNumber, setMessageNumber] = useState<number>(0);
    const [message, setMessage] = useState<string>("");

    useEffect(() => {
        setMessage(data.message[messageNumber].text)
    }, [])

    return (
        <>
            <div>
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