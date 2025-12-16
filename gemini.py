# # import os
# # import streamlit as st
# # from datetime import datetime

# # from langchain_google_genai import ChatGoogleGenerativeAI
# # from langchain_core.prompts import ChatPromptTemplate
# # from langchain_core.output_parsers import StrOutputParser

# # # Google GenAI Key
# # os.environ["GOOGLE_API_KEY"] = "AIzaSyDtC9dRuCaCb7_NL9RP4NFHz5PM5BZ6rXI"  # Add your Gemini key here

# # # LangSmith tracking
# # os.environ["LANGCHAIN_TRACING_V2"] = "true"
# # os.environ["LANGCHAIN_API_KEY"] = ""
# # os.environ["LANGCHAIN_PROJECT"] = "My-GenAI-Project-Gemini"

# # # Initialize session state for chat history
# # if "chat_sessions" not in st.session_state:
# #     st.session_state.chat_sessions = {}
# # if "current_session_id" not in st.session_state:
# #     st.session_state.current_session_id = None
# # if "session_counter" not in st.session_state:
# #     st.session_state.session_counter = 0

# # # Prompt template
# # prompt = ChatPromptTemplate.from_messages(
# #     [
# #         ("system", "I am a chatbot powered by Google Generative AI. Please type your queries."),
# #         ("user", "Question: {question}")
# #     ]
# # )

# # # Gemini LLM
# # llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
# # output_parser = StrOutputParser()
# # chain = prompt | llm | output_parser

# # # Sidebar for chat history
# # with st.sidebar:
# #     st.title("Chat History")

# #     # New Chat button
# #     if st.button("➕ New Chat", use_container_width=True):
# #         st.session_state.session_counter += 1
# #         new_session_id = f"session_{st.session_state.session_counter}"
# #         st.session_state.chat_sessions[new_session_id] = {
# #             "messages": [],
# #             "timestamp": datetime.now(),
# #             "title": f"Chat {st.session_state.session_counter}"
# #         }
# #         st.session_state.current_session_id = new_session_id
# #         st.rerun()

# #     st.divider()

# #     # Display chat sessions grouped by time
# #     if st.session_state.chat_sessions:
# #         now = datetime.now()
# #         today_sessions = []
# #         older_sessions = []

# #         for session_id, session_data in sorted(
# #             st.session_state.chat_sessions.items(),
# #             key=lambda x: x[1]["timestamp"],
# #             reverse=True
# #         ):
# #             time_diff = now - session_data["timestamp"]
# #             if time_diff.days == 0:
# #                 today_sessions.append((session_id, session_data))
# #             else:
# #                 older_sessions.append((session_id, session_data))

# #         # Today's chats
# #         if today_sessions:
# #             st.subheader("Today")
# #             for session_id, session_data in today_sessions:
# #                 col1, col2 = st.columns([4, 1])
# #                 with col1:
# #                     if st.button(
# #                         session_data["title"],
# #                         key=f"btn_{session_id}",
# #                         use_container_width=True,
# #                         type="primary" if session_id == st.session_state.current_session_id else "secondary"
# #                     ):
# #                         st.session_state.current_session_id = session_id
# #                         st.rerun()
# #                 with col2:
# #                     if st.button("🗑️", key=f"del_{session_id}"):
# #                         del st.session_state.chat_sessions[session_id]
# #                         if st.session_state.current_session_id == session_id:
# #                             st.session_state.current_session_id = None
# #                         st.rerun()

# #         # Older chats
# #         if older_sessions:
# #             st.divider()
# #             st.subheader("Older")
# #             for session_id, session_data in older_sessions:
# #                 col1, col2 = st.columns([4, 1])
# #                 with col1:
# #                     if st.button(
# #                         session_data["title"],
# #                         key=f"btn_{session_id}",
# #                         use_container_width=True,
# #                         type="primary" if session_id == st.session_state.current_session_id else "secondary"
# #                     ):
# #                         st.session_state.current_session_id = session_id
# #                         st.rerun()
# #                 with col2:
# #                     if st.button("🗑️", key=f"del_{session_id}"):
# #                         del st.session_state.chat_sessions[session_id]
# #                         if st.session_state.current_session_id == session_id:
# #                             st.session_state.current_session_id = None
# #                         st.rerun()
# #     else:
# #         st.info("No chat history yet. Start a new chat!")

# # # Main chat interface
# # st.title("LLM - GOOGLE GENAI PROJECT (Gemini Model) - By Tarun")

# # # Create a session if none exists
# # if not st.session_state.current_session_id:
# #     st.session_state.session_counter += 1
# #     new_session_id = f"session_{st.session_state.session_counter}"
# #     st.session_state.chat_sessions[new_session_id] = {
# #         "messages": [],
# #         "timestamp": datetime.now(),
# #         "title": f"Chat {st.session_state.session_counter}"
# #     }
# #     st.session_state.current_session_id = new_session_id

# # # Get current session
# # current_session = st.session_state.chat_sessions[st.session_state.current_session_id]

# # # Display chat messages
# # for msg in current_session["messages"]:
# #     with st.chat_message(msg["role"]):
# #         st.write(msg["content"])

# # # Chat input
# # input_text = st.chat_input("How may I help you?")

# # if input_text:
# #     # Add user message to chat
# #     current_session["messages"].append({"role": "user", "content": input_text})
# #     with st.chat_message("user"):
# #         st.write(input_text)

# #     # Get AI response
# #     with st.chat_message("assistant"):
# #         with st.spinner("Thinking..."):
# #             response = chain.invoke({"question": input_text})
# #             st.write(response)

# #     # Add assistant message to chat
# #     current_session["messages"].append({"role": "assistant", "content": response})

# #     # Update chat title with first message
# #     if len(current_session["messages"]) == 2:
# #         current_session["title"] = input_text[:30] + ("..." if len(input_text) > 30 else "")

# #     st.rerun()

# import os
# import streamlit as st
# from datetime import datetime

# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# # Google GenAI Key
# os.environ["GOOGLE_API_KEY"] = "AIzaSyDtC9dRuCaCb7_NL9RP4NFHz5PM5BZ6rXI"  # Add your Gemini key here

# # LangSmith tracking
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = ""
# os.environ["LANGCHAIN_PROJECT"] = "My-GenAI-Project-Gemini"

# # Page config
# st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖", layout="wide")

# # Custom CSS for better styling
# st.markdown("""
# <style>
#     /* Reduce font sizes */
#     .main h1 {
#         font-size: 1.8rem !important;
#         background: linear-gradient(180deg, #1e1e2e 0%, #2d2d44 100%);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         font-weight: 700;
#     }

#     .sidebar .element-container {
#         font-size: 0.85rem;
#     }

#     h2, h3 {
#         font-size: 1.1rem !important;
#         font-weight: 600;
#     }

#     /* Sidebar styling */
#     [data-testid="stSidebar"] {
#         background: linear-gradient(180deg, #1e1e2e 0%, #2d2d44 100%);
#     }

#     [data-testid="stSidebar"] h1 {
#         font-size: 1.3rem !important;
#         color: #ffffff;
#         font-weight: 600;
#     }

#     /* Chat message styling */
#     .stChatMessage {
#         font-size: 0.9rem;
#         padding: 0.8rem;
#         border-radius: 10px;
#     }

#     /* Button styling */
#     .stButton button {
#         font-size: 0.85rem;
#         border-radius: 8px;
#         transition: all 0.3s ease;
#     }

#     .stButton button:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 4px 12px rgba(0,0,0,0.15);
#     }

#     /* Input styling */
#     .stChatInput {
#         font-size: 0.9rem;
#     }

#     /* Divider */
#     hr {
#         margin: 0.8rem 0;
#         opacity: 0.3;
#     }

#     /* Compact spacing */
#     .element-container {
#         margin-bottom: 0.5rem;
#     }

#     /* Session button custom style */
#     div[data-testid="column"] button {
#         text-align: left !important;
#         font-size: 0.8rem !important;
#     }
# </style>
# """, unsafe_allow_html=True)

# # Initialize session state
# if "chat_sessions" not in st.session_state:
#     st.session_state.chat_sessions = {}
# if "current_session_id" not in st.session_state:
#     st.session_state.current_session_id = None
# if "session_counter" not in st.session_state:
#     st.session_state.session_counter = 0

# # Prompt template
# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "I am a chatbot powered by Google Generative AI. Please type your queries."),
#         ("user", "Question: {question}")
#     ]
# )

# # Gemini LLM
# llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
# output_parser = StrOutputParser()
# chain = prompt | llm | output_parser

# # Sidebar for chat history
# with st.sidebar:
#     st.markdown("### 💬 Chat History")

#     # New Chat button with icon
#     if st.button("✨ New Chat", use_container_width=True, type="primary"):
#         st.session_state.session_counter += 1
#         new_session_id = f"session_{st.session_state.session_counter}"
#         st.session_state.chat_sessions[new_session_id] = {
#             "messages": [],
#             "timestamp": datetime.now(),
#             "title": f"New conversation"
#         }
#         st.session_state.current_session_id = new_session_id
#         st.rerun()

#     st.divider()

#     # Display chat sessions
#     if st.session_state.chat_sessions:
#         now = datetime.now()
#         today_sessions = []
#         older_sessions = []

#         for session_id, session_data in sorted(
#             st.session_state.chat_sessions.items(),
#             key=lambda x: x[1]["timestamp"],
#             reverse=True
#         ):
#             time_diff = now - session_data["timestamp"]
#             if time_diff.days == 0:
#                 today_sessions.append((session_id, session_data))
#             else:
#                 older_sessions.append((session_id, session_data))

#         # Today's chats
#         if today_sessions:
#             st.markdown("**📅 Today**")
#             for session_id, session_data in today_sessions:
#                 col1, col2 = st.columns([5, 1])
#                 with col1:
#                     # Truncate title for display
#                     display_title = session_data["title"][:35] + "..." if len(session_data["title"]) > 35 else session_data["title"]
#                     button_type = "primary" if session_id == st.session_state.current_session_id else "secondary"

#                     if st.button(
#                         f"💬 {display_title}",
#                         key=f"btn_{session_id}",
#                         use_container_width=True,
#                         type=button_type
#                     ):
#                         st.session_state.current_session_id = session_id
#                         st.rerun()
#                 with col2:
#                     if st.button("🗑️", key=f"del_{session_id}", help="Delete chat"):
#                         del st.session_state.chat_sessions[session_id]
#                         if st.session_state.current_session_id == session_id:
#                             st.session_state.current_session_id = None
#                         st.rerun()

#         # Older chats
#         if older_sessions:
#             st.divider()
#             st.markdown("**📂 Older**")
#             for session_id, session_data in older_sessions:
#                 col1, col2 = st.columns([5, 1])
#                 with col1:
#                     display_title = session_data["title"][:35] + "..." if len(session_data["title"]) > 35 else session_data["title"]
#                     button_type = "primary" if session_id == st.session_state.current_session_id else "secondary"
#                     days_ago = (now - session_data["timestamp"]).days

#                     if st.button(
#                         f"💬 {display_title}",
#                         key=f"btn_{session_id}",
#                         use_container_width=True,
#                         type=button_type,
#                         help=f"{days_ago} day{'s' if days_ago > 1 else ''} ago"
#                     ):
#                         st.session_state.current_session_id = session_id
#                         st.rerun()
#                 with col2:
#                     if st.button("🗑️", key=f"del_{session_id}", help="Delete chat"):
#                         del st.session_state.chat_sessions[session_id]
#                         if st.session_state.current_session_id == session_id:
#                             st.session_state.current_session_id = None
#                         st.rerun()
#     else:
#         st.info("💡 No chats yet. Start a new conversation!")

#     # Footer
#     st.divider()
#     st.markdown("""
#     <div style='text-align: center; font-size: 0.75rem; opacity: 0.7;'>
#         🤖 Powered by Gemini AI<br>
#         Made with ❤️ by Tarun
#     </div>
#     """, unsafe_allow_html=True)

# # Main chat interface
# col1, col2, col3 = st.columns([1, 6, 1])
# with col2:
#     st.markdown("# 🤖 Gemini AI Chatbot")
#     st.markdown("*Your intelligent conversation partner*")

# # Create a session if none exists
# if not st.session_state.current_session_id:
#     st.session_state.session_counter += 1
#     new_session_id = f"session_{st.session_state.session_counter}"
#     st.session_state.chat_sessions[new_session_id] = {
#         "messages": [],
#         "timestamp": datetime.now(),
#         "title": "New conversation"
#     }
#     st.session_state.current_session_id = new_session_id

# # Get current session
# current_session = st.session_state.chat_sessions[st.session_state.current_session_id]

# # Display chat messages
# chat_container = st.container()
# with chat_container:
#     if not current_session["messages"]:
#         st.markdown("""
#         <div style='text-align: center; padding: 3rem; opacity: 0.6;'>
#             <h3>👋 Hello! How can I help you today?</h3>
#             <p>Ask me anything and let's start a conversation!</p>
#         </div>
#         """, unsafe_allow_html=True)
#     else:
#         for msg in current_session["messages"]:
#             with st.chat_message(msg["role"], avatar="🧑" if msg["role"] == "user" else "🤖"):
#                 st.write(msg["content"])

# # Chat input
# input_text = st.chat_input("💭 Type your message here...")

# if input_text:
#     # Add user message to chat
#     current_session["messages"].append({"role": "user", "content": input_text})
#     with st.chat_message("user", avatar="🧑"):
#         st.write(input_text)

#     # Get AI response
#     with st.chat_message("assistant", avatar="🤖"):
#         with st.spinner("🤔 Thinking..."):
#             response = chain.invoke({"question": input_text})
#             st.write(response)

#     # Add assistant message to chat
#     current_session["messages"].append({"role": "assistant", "content": response})

#     # Update chat title with first message
#     if len(current_session["messages"]) == 2:
#         current_session["title"] = input_text[:40] + ("..." if len(input_text) > 40 else "")

#     st.rerun()

import os
import streamlit as st
from datetime import datetime

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Google GenAI Key
os.environ["GOOGLE_API_KEY"] = ""

# LangSmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = ""
os.environ["LANGCHAIN_PROJECT"] = "My-GenAI-Project-Gemini"

# Page configuration
st.set_page_config(
    page_title="Gemini Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
<style>
    /* Main title styling */
    .main h1 {
        font-size: 1.8rem !important;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    /* Subtitle styling */
    .main h3 {
        font-size: 1rem !important;
        color: #718096;
        font-weight: 400;
        margin-top: 0;
    }
    
    /* Sidebar styling - Light theme */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f0f4ff 0%, #e8ecff 100%);
    }
    
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #2d3748 !important;
        font-size: 1.2rem !important;
        font-weight: 600;
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: #2d3748;
        font-size: 0.85rem;
    }
    
    [data-testid="stSidebar"] .stMarkdown strong {
        color: #1a202c;
        font-size: 0.9rem;
    }
    
    /* Chat message styling */
    .stChatMessage {
        font-size: 0.95rem;
        padding: 1rem;
        border-radius: 12px;
        margin-bottom: 0.5rem;
    }
    
    /* Button styling */
    .stButton button {
        font-size: 0.85rem;
        border-radius: 8px;
        transition: all 0.3s ease;
        font-weight: 500;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    /* Primary button in sidebar */
    [data-testid="stSidebar"] button[kind="primary"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border: none;
    }
    
    /* Chat input styling */
    .stChatInput input {
        font-size: 0.95rem;
        border-radius: 10px;
    }
    
    /* Divider styling */
    hr {
        margin: 1rem 0;
        opacity: 0.2;
        border-color: #cbd5e0;
    }
    
    /* Compact spacing */
    .element-container {
        margin-bottom: 0.5rem;
    }
    
    /* Session button alignment */
    div[data-testid="column"] button {
        text-align: left !important;
        font-size: 0.8rem !important;
    }
    
    /* Info box styling */
    .stInfo {
        background-color: #ebf4ff;
        border-left: 4px solid #667eea;
        font-size: 0.85rem;
    }
    
    /* Welcome message */
    .welcome-box {
        text-align: center;
        padding: 3rem 2rem;
        opacity: 0.7;
    }
    
    .welcome-box h3 {
        color: #2d3748;
        font-size: 1.5rem;
        margin-bottom: 0.5rem;
    }
    
    .welcome-box p {
        color: #718096;
        font-size: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "chat_sessions" not in st.session_state:
    st.session_state.chat_sessions = {}
if "current_session_id" not in st.session_state:
    st.session_state.current_session_id = None
if "session_counter" not in st.session_state:
    st.session_state.session_counter = 0

# Initialize LangChain components
prompt = ChatPromptTemplate.from_messages([
    ("system", "I am a chatbot powered by Google Generative AI. Please type your queries."),
    ("user", "Question: {question}")
])

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown("### 💬 Chat History")

    # New Chat button
    if st.button("✨ New Chat", use_container_width=True, type="primary"):
        st.session_state.session_counter += 1
        new_session_id = f"session_{st.session_state.session_counter}"
        st.session_state.chat_sessions[new_session_id] = {
            "messages": [],
            "timestamp": datetime.now(),
            "title": "New conversation"
        }
        st.session_state.current_session_id = new_session_id
        st.rerun()

    st.divider()

    # Display chat sessions grouped by time
    if st.session_state.chat_sessions:
        now = datetime.now()
        today_sessions = []
        older_sessions = []

        # Categorize sessions
        for session_id, session_data in sorted(
            st.session_state.chat_sessions.items(),
            key=lambda x: x[1]["timestamp"],
            reverse=True
        ):
            time_diff = now - session_data["timestamp"]
            if time_diff.days == 0:
                today_sessions.append((session_id, session_data))
            else:
                older_sessions.append((session_id, session_data))

        # Display Today's chats
        if today_sessions:
            st.markdown("**📅 Today**")
            for session_id, session_data in today_sessions:
                col1, col2 = st.columns([5, 1])
                with col1:
                    display_title = session_data["title"][:35] + "..." if len(
                        session_data["title"]) > 35 else session_data["title"]
                    button_type = "primary" if session_id == st.session_state.current_session_id else "secondary"

                    if st.button(
                        f"💬 {display_title}",
                        key=f"btn_{session_id}",
                        use_container_width=True,
                        type=button_type
                    ):
                        st.session_state.current_session_id = session_id
                        st.rerun()

                with col2:
                    if st.button("🗑️", key=f"del_{session_id}", help="Delete chat"):
                        del st.session_state.chat_sessions[session_id]
                        if st.session_state.current_session_id == session_id:
                            st.session_state.current_session_id = None
                        st.rerun()

        # Display Older chats
        if older_sessions:
            st.divider()
            st.markdown("**📂 Older**")
            for session_id, session_data in older_sessions:
                col1, col2 = st.columns([5, 1])
                with col1:
                    display_title = session_data["title"][:35] + "..." if len(
                        session_data["title"]) > 35 else session_data["title"]
                    button_type = "primary" if session_id == st.session_state.current_session_id else "secondary"
                    days_ago = (now - session_data["timestamp"]).days

                    if st.button(
                        f"💬 {display_title}",
                        key=f"btn_{session_id}",
                        use_container_width=True,
                        type=button_type,
                        help=f"{days_ago} day{'s' if days_ago > 1 else ''} ago"
                    ):
                        st.session_state.current_session_id = session_id
                        st.rerun()

                with col2:
                    if st.button("🗑️", key=f"del_{session_id}", help="Delete chat"):
                        del st.session_state.chat_sessions[session_id]
                        if st.session_state.current_session_id == session_id:
                            st.session_state.current_session_id = None
                        st.rerun()
    else:
        st.info("💡 No chats yet. Start a new conversation!")

    # Footer
    st.divider()
    st.markdown("""
    <div style='text-align: center; font-size: 0.75rem; color: #718096;'>
        🤖 Powered by Gemini AI<br>
        Made with ❤️ by Tarun
    </div>
    """, unsafe_allow_html=True)

# ==================== MAIN CHAT INTERFACE ====================

# Header
col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    st.markdown("# 🤖 Gemini AI Chatbot")
    st.markdown("*Your intelligent conversation partner*")

# Create initial session if none exists
if not st.session_state.current_session_id:
    st.session_state.session_counter += 1
    new_session_id = f"session_{st.session_state.session_counter}"
    st.session_state.chat_sessions[new_session_id] = {
        "messages": [],
        "timestamp": datetime.now(),
        "title": "New conversation"
    }
    st.session_state.current_session_id = new_session_id

# Get current session
current_session = st.session_state.chat_sessions[st.session_state.current_session_id]

# Display chat messages or welcome message
chat_container = st.container()
with chat_container:
    if not current_session["messages"]:
        st.markdown("""
        <div class='welcome-box'>
            <h3>👋 Hello! How can I help you today?</h3>
            <p>Ask me anything and let's start a conversation!</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        for msg in current_session["messages"]:
            with st.chat_message(msg["role"], avatar="🧑" if msg["role"] == "user" else "🤖"):
                st.write(msg["content"])

# Chat input
input_text = st.chat_input("💭 Type your message here...")

if input_text:
    # Add user message
    current_session["messages"].append({"role": "user", "content": input_text})
    with st.chat_message("user", avatar="🧑"):
        st.write(input_text)

    # Generate AI response
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("🤔 Thinking..."):
            response = chain.invoke({"question": input_text})
            st.write(response)

    # Add assistant message
    current_session["messages"].append(
        {"role": "assistant", "content": response})

    # Update chat title with first user message
    if len(current_session["messages"]) == 2:
        current_session["title"] = input_text[:40] + \
            ("..." if len(input_text) > 40 else "")

    st.rerun()
