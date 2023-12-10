import os
import openai
from dotenv import load_dotenv, find_dotenv
import re

_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']


def exam_prep(token):
    # print(token.STATE)
    print('----------------------------------')
    print(f'>>>>>>>>>>>>>>STATE keys: {token.STATE.keys()}>>>>>>>>>>>>>>')
    print('----------------------------------')
    if token.STATE['STATE'] == 'multiple_choice':

        question = f"""


        Q1
        {token.mpc_1}
        Q2
        {token.mpc_2}
        Q3
        {token.mpc_3}
        Q4
        {token.mpc_4}
        Q5
        {token.mpc_5}

        """


    elif token.STATE['STATE'] == 'short_essay':

        question = f"""
        ### Short Essay Questions

        1. **{token.short_essay_1}**
        ---
        2. **{token.short_essay_2}**
        ---
        """

    elif token.STATE['STATE'] == 'scenario_essay':

        question = f"""
        Please answer write an essay on the following topic:

        {token.scenario}
        """


    token.exam_questions = question

    return token




def exam_correction(token):
    print('entering exam correction')
    system_message = """
    You are an assistant helping a student prepare for their International Baccalaureate (IB) Economics final exam.
    This exam includes multiple choice questions, short essay questions, and longer scenario-based essay questions.
    Your role is to review the student's responses, provide corrections where necessary, and offer explanations to help clarify any misunderstandings.
    """
    messages = [{'role':'system', 'content': system_message},
                {'role':'user', 'content': 'Could you help me review some practice questions for my IB Economics final exam?'},
                {'role': 'assistant', 'content': token.exam_questions},
                {'role':'user', 'content': token.user_text}]
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.8,
            max_tokens=500
        )
    answer = response.choices[0].message["content"]
    token.exam_correction = answer

    return token

if __name__ == "__main__":
    print("test")
