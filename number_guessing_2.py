from autogen import ConversableAgent, UserProxyAgent
from llm_config import llm_config

agent_with_number_term = ConversableAgent(
    "agent_with_number_term",
    system_message=(
        "You are playing a game of guess-my-number. You have the number 58 in your mind, "
        "and I will try to guess it.\n"
        "If my guess is much higher than your number, say 'too high'.\n"
        "If my guess is much lower than your number, say 'too low'.\n"
        "If my guess is only slightly higher (within 5), say 'high'.\n"
        "If my guess is only slightly lower (within 5), say 'low'.\n"
        "If I guess correctly, say 'correct'."
    ),
    llm_config=llm_config,
    max_consecutive_auto_reply=2,
    is_termination_msg=lambda msg: "58" in msg["content"],  # Terminate if the correct number is guessed
    human_input_mode="TERMINATE",  
)

agent_guess_number = ConversableAgent(
    "agent_guess_number",
    system_message=(
        "I have a number in my mind, and you will try to guess it. "
        "If I say 'too high', you should guess a much lower number. "
        "If I say 'high', you should guess a slightly lower number. "
        "If I say 'too low', you should guess a much higher number. "
        "If I say 'low', you should guess a slightly higher number. "
        "Keep adjusting your guess based on the feedback until you get it right."
    ),
    is_termination_msg = lambda msg: 'correct' in msg['content'].lower(),
    llm_config=llm_config,
    human_input_mode="NEVER",
)

agent_with_number_term.initiate_chat(
    agent_guess_number,
    message="I have a number between 1 and 100. Guess it!",
)
