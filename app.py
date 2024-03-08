import streamlit as st

# Import your chatbot model or logic
# from my_chatbot import Chatbot

# Create a Streamlit app
def main():
    st.title("Chatbot Interface")

    # Initialize your chatbot
    # chatbot = Chatbot()

    # Text input for user to enter messages
    user_input = st.text_input("You:", "")

    if st.button("Send"):
        if(user_input):
            print(user_input)

if __name__ == "__main__":
    main()