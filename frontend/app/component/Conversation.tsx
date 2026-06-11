import useChatStore from "~/stores/useChatStore";
import ChatBalloon from "./ChatBalloon";

const Conversation = () => {

    const chat = useChatStore();



    return (
        <>
            <div className="flex flex-col gap-5">
                {
                    chat.contents.map((item, index) => {
                        return <ChatBalloon key={index} message={item.content} role={item.role}/>
                    })
                }
            </div>
        </>
    );
}

export default Conversation