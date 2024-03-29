
import openai
import os
from dotenv import load_dotenv, find_dotenv
import time
from states import Token
import streamlit as st

_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key  = os.getenv('OPENAI_API_KEY')

button_style = """
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color: white;
}
div.stButton > button:first-child:hover {
    background-color: #0077cc;
}
</style>
"""


def main():
    st.title("Pim de Ridder's IB Test Practice")
    st.markdown(button_style, unsafe_allow_html=True)

    if 'usage_count' not in st.session_state:
        st.session_state['usage_count'] = 0

    exam_type = st.selectbox("Choose your exam", [None, "multiple_choice", "short_essay", "scenario_essay"])

    if exam_type:
        if st.session_state['usage_count'] < 15:

            if 'token' not in st.session_state or st.session_state['restart']:
                st.session_state['token'] = Token(STATE=exam_type)
                st.session_state['restart'] = False

            token = st.session_state['token']
            token = token.STATE.get("function")(token)
            st.write(token.exam_questions)

            # token.user_text = st.text_area("Your answer", height=300)
            placeholder_text = "Enter your answer here..."

            with st.form("prompt_form", clear_on_submit=True):
                token.user_text = st.text_area("Your Answer:", placeholder=placeholder_text, height=300)
                prompt_submitted = st.form_submit_button("Check Answer")

            if prompt_submitted:
                st.session_state['usage_count'] += 1
                token.change_state('correction')
                token = token.STATE.get("function")(token)
                st.write(token.exam_correction)

            # token.change_state('correction')
            # if st.button("Check Answer"):
            #     st.session_state['usage_count'] += 1
            #     token = token.STATE.get("function")(token)
            #     st.write(token.exam_correction)

            if st.button("Try Another Question"):
                for key in list(st.session_state.keys()):
                    if key not in ['usage_count']:
                        del st.session_state[key]


                st.experimental_rerun()

        else:
            st.write("You have reached the maximum usage limit for this session.")


if __name__ == "__main__":
    main()
