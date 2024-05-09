print("""
    _   __     __          __     
   / | / /__  / /_  __  __/ /___ _
  /  |/ / _ \\/ __ \\/ / / / / __ `/
 / /|  /  __/ /_/ / /_/ / / /_/ / 
/_/ |_/\\___/_.___/\\__,_/_/\\__,_/ 
      
      """)

print("<System> Initializing virtual machine...\n")

from transformers import pipeline, Conversation as conv

firstmsg = True
global conversation

print("<System> Loading tokenizer and model...\n")

Nebula = pipeline(model="facebook/blenderbot-400M-distill")

def generate(user_input):
    global firstmsg
    global conversation
    if firstmsg:
        conversation = conv(user_input)
        firstmsg = False
    else:
        conversation.add_message({"role": "user", "content": user_input})
    response = Nebula(user_input)
    return response[-1]['generated_text']

print("\n<System> Offline mode activated. Ready for computing locally.")
print("<System> Virtual machine has been initialized. Please enter a command to begin.")
print("<System> Type 'exit' to end the conversation.")
print("<System> Press Ctrl+C to force shutdown the virtual machine.\n")

try:
    while True:
        user_input = input("> ")
        if user_input.lower() == "exit":
            print("<System> Exiting virtual machine...\nGoodbye!")
            exit()
        response = generate(user_input)
        print("<Nebula>", response)
except KeyboardInterrupt:
    print("\n<System> Force shutting down virtual machine...\nGoodbye!")
    exit()