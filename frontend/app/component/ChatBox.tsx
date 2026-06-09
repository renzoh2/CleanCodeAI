
const ChatBox = () => {

    const greeting = [
        "Ask Anything",
        "How can I help you?"
    ];

    const greetingNumber = Math.floor(Math.random() * 2);

    return (
        <>
            <div className="flex grow">
                <div className="flex flex-col w-full">
                    <div className="py-5 px-10">
                        NAVBAR HERE
                    </div>
                    <form>
                        <input className="" placeholder={greeting[greetingNumber]} />
                        <button type="submit">
                            SEND
                        </button>
                    </form>
                </div>
            </div>
        </>
    );
}

export default ChatBox;