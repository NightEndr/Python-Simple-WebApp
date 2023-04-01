import gradio
def greet(name):
    return 'hi, '+name+', this is your first step on WebApp.'

app=gradio.Interface(
    inputs="text",
    fn=greet,
    outputs="text"
)

app.launch(share=True)