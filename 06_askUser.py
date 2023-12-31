import chainlit as cl


@cl.on_chat_start
async def main():
    res = await cl.AskUserMessage(content="What is your name?", timeout=1).send()
    if res:
        await cl.Message(
            content=f"Your name is: {res['content']}",
        ).send()
