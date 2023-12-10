from dotenv import load_dotenv, find_dotenv
import numpy as np
import random
from final_mpc import MPC_QUESTIONS
from final_short_essay import SHORT_ESSAYS
from final_scenario_essay import SCENARIO_QUESTIONS

from exam_tester import exam_prep, exam_correction
question_index = np.random.choice(range(25), size=2, replace=False)
q1 = question_index[0]
q2 = question_index[1]

question_index = np.random.choice(range(82), size=5, replace=False)
q1_short = question_index[0]
q2_short = question_index[1]


#====================STATES===================
multiple_choice = {'STATE': 'multiple_choice' ,'mpc_1': MPC_QUESTIONS,'mpc_2': MPC_QUESTIONS, 'mpc_3': MPC_QUESTIONS, 'mpc_4': MPC_QUESTIONS, 'mpc_5': MPC_QUESTIONS, "function": exam_prep}
short_essay = {'STATE': 'short_essay','short_essay_1': SHORT_ESSAYS, 'short_essay_2': SHORT_ESSAYS, "function": exam_prep}
scenario_essay = {'STATE': 'scenario_essay' , 'scenario': SCENARIO_QUESTIONS, "function": exam_prep}
correction = {"function": exam_correction}

module_review = { "function": 1234}

# #====================STATES_DICTIONARY===================
STATES_DICTIONARY = {
    "multiple_choice": multiple_choice,
    "short_essay": short_essay,
    "scenario_essay": scenario_essay ,
    "correction": correction,
    "module_review": module_review,
    }


#====================TOKEN===================
class Token():

    def __init__(self, STATE="multiple_choice"):
        question_index = np.random.choice(range(32), size=2, replace=False)
        q1 = question_index[0]
        q2 = question_index[1]

        question_index = np.random.choice(range(82), size=5, replace=False)
        q1_mpc = question_index[0]
        q2_mpc = question_index[1]
        q3_mpc = question_index[2]
        q4_mpc = question_index[3]
        q5_mpc = question_index[4]

        question_index = np.random.choice(range(9), size=1, replace=False)
        scenario_idx = question_index

        self.STATE = STATES_DICTIONARY[STATE]
        self.audio = None
        self.messages = None
        self.user_text = None
        self.system_text = None
        self.message_count = 0
        self.active = True
        self.loops = 0
        self.errors = 0

        if STATE == 'multiple_choice':
            self.mpc_1 = STATES_DICTIONARY[STATE]['mpc_1'][q1_mpc]
            self.mpc_2 = STATES_DICTIONARY[STATE]['mpc_2'][q2_mpc]
            self.mpc_3 = STATES_DICTIONARY[STATE]['mpc_1'][q3_mpc]
            self.mpc_4 = STATES_DICTIONARY[STATE]['mpc_2'][q4_mpc]
            self.mpc_5 = STATES_DICTIONARY[STATE]['mpc_1'][q5_mpc]
        elif STATE == 'short_essay':
            self.short_essay_1 = STATES_DICTIONARY[STATE]['short_essay_1'][q2]
            self.short_essay_2 = STATES_DICTIONARY[STATE]['short_essay_1'][q1]
        elif STATE == 'scenario_essay':
            self.scenario = STATES_DICTIONARY[STATE]['scenario'][scenario_idx[0]]
        self.assistant_message = None
        self.hallucinate = False
        self.interrupted = False
        self.exam_correction = None

    def turn_off(self):
        self.active = False

    def add_message(self, messages):
        if isinstance(messages, list):
            if self.messages is None:
                self.messages = messages
            else:
                self.messages.extend(messages)
        else:
            if self.messages is None:
                self.messages = [messages]
            else:
                self.messages.append(messages)

    def clear_messages(self):
        self.messages = None

    def increase_message_count(self):
        self.message_count += 1

    def add_loop(self):
        self.loops += 1

    def increase_error_count(self):
        self.errors += 1

    def change_state(self, text):
        if text in STATES_DICTIONARY:
            self.STATE = STATES_DICTIONARY[text]



if __name__ == "__main__":
    token = Token(STATE="mid_term_1")
    print(token.__dict__)
    # token.system_text = "There are seventeen pirates in the basement"
    # token.user_text = "translate the text please"
    # token = book(token)
