//State Manager
import { create  } from 'zustand'

interface MessageIterationInterface {
    iteration: number;
    text: string;
}

interface MessageContentInterface {
    role: string;
    content: MessageIterationInterface[];
}

interface ChatStoreInterface {
    contents: MessageContentInterface[];
    addContent: (newContent: MessageContentInterface) => void;
    restartContent: () => void;
}

const useChatStore = create<ChatStoreInterface>((set) => ({
    contents: [],
    addContent: (newContent) => set((state) => ({contents: [...state.contents, newContent]})),
    restartContent: () => set({contents: []})
}))

export default useChatStore;