import chainlit as cl

@cl.on_chat_start
async def start():
    await cl.Message(content="This message is send in the start:").send()
