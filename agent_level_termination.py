from autogen import ConversableAgent
from llm_config import llm_config

maddy = ConversableAgent(
    "maddy",
    system_message = "Your name is Maddy and you are a part of a duo of comedians.",
    llm_config = llm_config,
    human_input_mode = "NEVER"
)

 # max consecutive auto reply
#joe = ConversableAgent(
#    "joe",
#    system_message = "Your name is Joe and you are a part of a duo of comedians.",
#    llm_config = llm_config,
#    human_input_mode = "NEVER",
#    max_consecutive_auto_reply=1
#)

#joe.initiate_chat(maddy, message = "Hi Maddy, tell me a joke.")

joe = ConversableAgent(
    "joe",
    system_message = "Your name is Joe and you are a part of a duo of comedians.",
    llm_config = llm_config,
    human_input_mode = "NEVER",
    is_termination_msg = lambda msg: "terminate" in msg["content"].lower(),
)

joe.initiate_chat(maddy, message = "Maddy, tell me a joke and then say the TERMINATE ")
