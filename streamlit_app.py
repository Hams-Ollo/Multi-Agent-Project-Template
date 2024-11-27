"""
Main entry point for Streamlit Cloud deployment
"""
import streamlit as st
import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

# Import the main frontend components
from frontend.Chat import main as chat_main
from frontend.pages import Home

def main():
    """Main function to run the Streamlit application."""
    # Set page config
    st.set_page_config(
        page_title="Dynamic AI Assistant",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Run the main chat interface
    chat_main()

if __name__ == "__main__":
    main()
