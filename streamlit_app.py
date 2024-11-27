"""
Main entry point for Streamlit Cloud deployment
"""
import os
import sys
from pathlib import Path

import streamlit as st

# Set page configuration at the very beginning
st.set_page_config(
    page_title="Dynamic AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Add the project root to the Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

# Import after st.set_page_config
from frontend.Chat import display_chat_interface

def init_session_state():
    """Initialize session state variables."""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

def main():
    """Main function to run the Streamlit application."""
    # Initialize session state
    init_session_state()
    
    # Set the app title in sidebar
    st.sidebar.markdown("# 💬 AI Chat Assistant")

    # Display the chat interface
    display_chat_interface()

if __name__ == "__main__":
    main()
