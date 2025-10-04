from autogen import ConversableAgent
from llm_config import llm_config

agent_with_number = ConversableAgent(
    "agent_with_number",
    system_message = "You are playing a number guessing game and you have the number 58 in your mind."
              "If the number guessed is too high, say too high."
              "If the number guessed is slightly high (within 5), say high."
              "If the number guessed is too low, say too low."
              "If the number guessed is slightly low (within 5), say low"
              "If I guess correctly, say 'correct'.",
    llm_config = llm_config,
    #is_termination_msg = lambda msg: '58' in msg['content'],
    human_input_mode = "NEVER"
)

agent_guessing = ConversableAgent(
    "agent_guessing",
    system_message = "You are playing a number guessing game and you have to guess a number each time."
              "If I say too high, you should guess a much lower number"
              "If I say high, you should guess a slightly lower number"
              "If I say too low, you should guess a much higher number"
              "If I say low, you shoud guess a slightly higher number"
              "Keep adjusting your guess based on the feedback until you get it right.",
    llm_config = llm_config,
    is_termination_msg = lambda msg: 'correct' in msg['content'].lower(),
    human_input_mode = "NEVER"
)

agent_with_number.initiate_chat(
    agent_guessing,
    message = "I have a number between 1 and 100. Guess it"    
)

