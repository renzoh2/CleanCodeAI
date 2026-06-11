//State Manager
import { create  } from 'zustand'

interface ChatStoreInterface {
    messages: string[];
    addMessage: (newMessage: string) => void;
}

const useChatStore = create<ChatStoreInterface>((set) => ({
    messages: [],
    addMessage: (newMessage) => set((state) => ({messages: [...state.messages, newMessage]}))
}))

export default useChatStore;