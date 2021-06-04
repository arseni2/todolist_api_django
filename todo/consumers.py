import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from todo.models import TodoListModel

# сделать так чтобы возвращались все записи можно сделать отдельный consumer
#сделать так чтобы по вебсокету возвращались все записи из модели
class TodoAddConsumer(AsyncWebsocketConsumer): #типа view на default django
    async def connect(self):
        print(self.scope)
        self.text = self.scope['url_route']['kwargs']['text']
        print(self.scope['url_route'])
        self.group_todo_name = 'todo_%s' % self.text
        print(self.text)
        print('eee' * 99) #channel_layer -- каналы
        await self.channel_layer.group_add(
            self.group_todo_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):  # когда происходит разрыв соеденения
        print(self.scope)
        async_to_sync(self.channel_layer.group_discard)(self.group_todo_name, self.channel_name)

    async def receive(self, text_data):  # получение данных
        text_data_json = json.loads(text_data)
        todo_text = text_data_json['text'] #в теории можно сереализовать все записи из модели и их возвращать

        new_todo = await self.create_todo(todo_text)

        data = {
            'text': new_todo.text,
            'is_importants': new_todo.is_importants,
            'is_delete': new_todo.is_delete,
            'is_complete': new_todo.is_complete,
            'editMode': new_todo.editMode,
        }
        await self.channel_layer.group_send(
            self.group_todo_name,
            {
                'type': 'new_todo',
                'message': data
            }
        )

    async def new_todo(self, event):  #отправка данных на клиент
        print('THIS IS EVENT FROM NEW_TODO', event)
        text = event['text']
        await self.send(
            text_data=json.dump({
                'text': text
            })
        )
    @database_sync_to_async
    def create_todo(self, text):
        print('THIS IS TEXT FROM CREATE_TODO', text)
        new_todo = TodoListModel.objects.create(
            text=text,
            is_importants=False,
            is_delete=False,
            is_complete=False,
            editMode=False,
        )
        return new_todo
