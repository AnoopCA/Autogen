import os
from autogen import AssistantAgent, UserProxyAgent
from llm_config import llm_config

assistant = AssistantAgent("assistant", llm_config=llm_config)
user_proxy = UserProxyAgent("user_proxy", code_execution_config=False)

user_proxy.initiate_chat(
    assistant,
    message= "Tell me a joke on data scientists"
)
