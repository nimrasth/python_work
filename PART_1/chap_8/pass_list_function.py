

# # messages
# def short_message(messages):
#     for m in messages:
#         print (m)
# message=['hello', 'good morning', 'good luck', 'bye']
# short_message(message)


# sending messages

def short_message(messages):
    for m in messages:
        print (m)
    
    
def send_message(messages):
    messages_copy = messages.copy()

    sent_message=[]
    print("\nThe sent messages are:")
    for every_message in messages_copy:
      
        print(every_message)
  
        sent_message.append(every_message)
        message.remove(every_message)
        print(messages)
        print(sent_message)

    # new = messages
    # for every_message in messages:
    #     messages.remove(every_message)
        

    # print(new)


message=['hello', 'good morning', 'good luck', 'bye']
short_message(message)
send_message(message)
