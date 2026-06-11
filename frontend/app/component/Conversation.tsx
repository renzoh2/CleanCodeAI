import useChatStore from "~/stores/useChatStore";

const Conversation = () => {

    const chat = useChatStore();

    return (
        <>
            <div>
                CONVERSATION BOX
                {
                    chat.messages.map((item, index) => {
                        return <p key={index}>{item}</p>
                    })
                }
            </div>
        </>
    );
}

export default Conversation