import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
def write_message(sender, message):
  authorize.method('messages.send', {'chat_id': sender, 'message': message, 'random_id': get_random_id()})
def get_name(from_id):
  sender_info = getting_api.users.get(user_ids = from_id)[0]
  full_name = sender_info.get('first_name') + ' ' + sender_info['last_name']
  return full_name
token = '931c2ba771d5c390e6062502bcf4cf7343f1d5049420860e5833f45375f80c68386ee97da78588b9fb168'
authorize = vk_api.VkApi(token = token)
longpoll = VkBotLongPoll(authorize, group_id=200870743)
getting_api = authorize.get_api()
for event in longpoll.listen():
  if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat and event.message.get('text') !="":
    reseived_message = event.message.get('text')
    sender = event.chat_id
    from_id = event.message.get('from_id')
    name = get_name(from_id)
    if reseived_message == 'Привет':
      write_message(sender, 'и тебе привет!' + ', ' + name)
    elif reseived_message == 'Пока':
      write_message(sender, 'чао какао')
    else:
      write_message(sender, 'Чаво чаво?')