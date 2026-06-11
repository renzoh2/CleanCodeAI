//State Manager
import { create  } from 'zustand'


interface MessageIterationInterface {
    iteration: number;
    text: string;
}

interface MessageContentInterface {
    role: string;
    message: MessageIterationInterface[];
}

interface ChatStoreInterface {
    contents: MessageContentInterface[];
    addContent: (newContent: MessageContentInterface) => void;
}

const useChatStore = create<ChatStoreInterface>((set) => ({
    contents: [],
    addContent: (newContent) => set((state) => ({contents: [...state.contents, newContent]}))
}))

export default useChatStore;