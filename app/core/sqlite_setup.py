"""
SQLite configuration for ChromaDB compatibility.
"""
import sys
import logging

def setup_sqlite():
    """
    Configure SQLite for ChromaDB compatibility.
    This function attempts to use pysqlite3 if available,
    which provides a newer SQLite version compatible with ChromaDB.
    """
    try:
        import pysqlite3
        import sqlite3

        logging.info("Setting up pysqlite3 for ChromaDB compatibility")
        
        # Check if we need to replace sqlite3
        current_version = sqlite3.sqlite_version_info
        required_version = (3, 35, 0)
        
        if current_version < required_version:
            logging.info(f"Current SQLite version {current_version} is older than required {required_version}")
            logging.info("Replacing sqlite3 with pysqlite3")
            
            # Replace sqlite3 with pysqlite3
            sys.modules['sqlite3'] = pysqlite3
            
            # Verify the replacement
            import sqlite3
            logging.info(f"Using SQLite version: {sqlite3.sqlite_version}")
        else:
            logging.info(f"Using system SQLite version: {current_version}")
            
    except ImportError:
        logging.warning("pysqlite3 not available, using system SQLite")
        # Continue with system sqlite3, ChromaDB will raise an error if version is incompatible
