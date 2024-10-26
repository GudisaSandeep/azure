
import streamlit as st

def main():
    st.title("My Azure Streamlit App")
    
    st.write("Welcome to my Azure-deployed Streamlit application!")
    
    # Add a simple interactive element
    user_input = st.text_input("Enter your name:")
    if user_input:
        st.write(f"Hello, {user_input}!")
    
    # Add a simple counter
    if 'count' not in st.session_state:
        st.session_state.count = 0
        
    st.write("Current count:", st.session_state.count)
    
    if st.button("Increment"):
        st.session_state.count += 1

if __name__ == "__main__":
    main()
