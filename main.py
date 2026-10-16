from ollama import chat


URl='http://localhost:11434/api/chat'
MODEL_NAME = 'phi3'

def chat_requests(messages):
    stream = chat(model=MODEL_NAME, messages=messages, stream=True)
    full_reply = ''
    for chunk in stream:
        piece = chunk['message']['content']
        print(piece, end='', flush=True)
        full_reply += piece
    return full_reply



def main():
    messages = [
        {
            'role': 'system',
            'content': "You are a helpful assistant. Answer short and clear"
        }
    ]
    print('phi-3 simple chat. Type exit to quit.')
    while True:
        user_input = input('You: ')
        if user_input == 'exit':
            print('Bye bye!')
            break
        messages.append({
            'role': 'user',
            'content': user_input
        })
        print('\nAssistant:', end='', flush=True)
        reply = chat_requests(messages)
        messages.append({
            'role': 'assistant',
            'content': reply
        })
        print()
        print('_' * 65)



main()