from autogen import ConversableAgent
from llm_config import llm_config

maddy = ConversableAgent(
    "maddy",
    system_message = "Your name is Maddy and you are a part of a duo of comedians.",
    llm_config = llm_config,
    human_input_mode = "NEVER"
)

joe = ConversableAgent(
    "joe",
    system_message = "Your name is Joe and you are a part of a duo of comedians.",
    llm_config = llm_config,
    human_input_mode = "NEVER"
)

# Passing max turns value and in initiat_chat method
joe.initiate_chat(maddy, message = "Maddy, tell me a joke.", max_turns = 2)
