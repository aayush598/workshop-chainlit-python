import chainlit as cl 

@cl.on_message
async def main(message: cl.Message):

    # Your custom logic goes here...
    text_content = "Hello, this is a element."

    elements = [
        cl.Text(name="simple_text", content=text_content, display="inline")
    ]

    # elements = [
    # cl.Image(name="image1", display="inline", path="MultiMedia/image.png")
    # ]

    # elements = [
    # cl.Pdf(name="pdf1", display="inline", path="MultiMedia/file.pdf")
    # ]
    # Send a response back to the user
    await cl.Message(
        content="Check out this element!", elements=elements
    ).send()