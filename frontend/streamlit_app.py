"""
Streamlit frontend for the AI Chat Interface.
"""
import sys
import os
from pathlib import Path

# Add parent directory to path to import app modules
sys.path.append(str(Path(__file__).parent.parent))

import streamlit as st
from app.agents.chat_agent import ChatAgent
from app.utils.memory import MemoryManager
from app.core.config import load_config
from colorama import Fore, Style

def initialize_chat_system():
    """Initialize the chat system components."""
    try:
        print(f"\n{Fore.CYAN}🚀 Initializing AI Chat System...{Style.RESET_ALL}")
        config = load_config()
        
        print(f"{Fore.CYAN}📚 Initializing Memory System...{Style.RESET_ALL}")
        memory_manager = MemoryManager(config.get('memory', {}))
        
        print(f"{Fore.CYAN}🤖 Initializing AI Agent...{Style.RESET_ALL}")
        agent = ChatAgent(config.get('agent', {}))
        agent.initialize(memory_manager)
        
        print(f"{Fore.GREEN}✨ Chat system initialized successfully!{Style.RESET_ALL}")
        return agent
    except Exception as e:
        st.error(f"Error initializing chat system: {str(e)}")
        return None

def main():
    """Main Streamlit application."""
    # Page configuration
    st.set_page_config(
        page_title="AI Chat Interface",
        page_icon="🤖",
        layout="wide"
    )

    # Header
    st.title("🤖 AI Chat Interface")
    st.markdown("### 🧠 Powered by Groq LLM & LangChain")
    
    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "agent" not in st.session_state:
        st.session_state.agent = initialize_chat_system()
        if st.session_state.agent is None:
            st.error("Failed to initialize chat system. Please check your configuration and try again.")
            return

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get AI response
        with st.chat_message("assistant"):
            with st.spinner("🤔 AI is thinking..."):
                try:
                    response = st.session_state.agent.process_message(prompt)
                    ai_response = response.get("response", "I apologize, but I encountered an error processing your message.")
                    st.markdown(ai_response)
                    st.session_state.messages.append({"role": "assistant", "content": ai_response})
                except Exception as e:
                    error_message = f"Error generating response: {str(e)}"
                    st.error(error_message)
                    st.session_state.messages.append({"role": "assistant", "content": f"❌ {error_message}"})

    # Add a clear chat button
    if st.sidebar.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    # Add helpful information in the sidebar
    with st.sidebar:
        st.markdown("### 💡 Tips")
        st.markdown("""
        - Type 'help' for available commands
        - Use clear chat button to start fresh
        - Questions are answered using context and general knowledge
        """)

if __name__ == "__main__":
    main()
