import requests

URl='http://localhost:11434/api/chat'
MODEL_NAME = 'phi3'

def chat_requests(messages):
    payload = {
        'model': MODEL_NAME,
        'messages': messages,
        'stream': False,
    }
    response = requests.post(URl, json=payload)
    response.raise_for_status()
    data = response.json()
    return data['message']['content']

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
        reply = chat_requests(messages)
        messages.append({
            'role': 'assistant',
            'content': reply
        })
        print('\nAssistant:', reply)
        print('_' * 60)



main()