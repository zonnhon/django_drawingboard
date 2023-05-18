# import json
# from asgiref.sync import async_to_sync
# from channels.generic.websocket import AsyncWebsocketConsumer
#
# class DrawingConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_name = 'drawing'
#         self.room_group_name = 'group_drawing'
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name, self.room_name
#         )
#         await self.accept()
#
#     async def disconnect(self, close_code):
#         # pass
#         await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
#
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         x = text_data_json['x']
#         y = text_data_json['y']
#         color = text_data_json['color']
#         is_drawing = text_data_json['is_drawing']
#         await self.channel_layer.group_send(
#             self.room_group_name, {"type": "chat.message", "message": message}
#         )
#
#         await self.send(text_data=json.dumps({
#             'x': x,
#             'y': y,
#             'color': color,
#             'is_drawing': is_drawing,
#         }))

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class DrawingBoardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('connect')
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'drawing_board_{self.room_name}'

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        print('disconnect')
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # async def receive(self, text_data):
    #     print('receive')
    #     text_data_json = json.loads(text_data)
    #     action = text_data_json['action']
    #     x = text_data_json['x']
    #     y = text_data_json['y']
    #     print('receive', action, x, y)
    #     await self.channel_layer.group_send(self.room_group_name, {'type': 'broadcast', 'action': action, 'x': x, 'y': y})
    #
    # async def broadcast(self, event):
    #
    #     action = event['action']
    #     x = event['x']
    #     y = event['y']
    #     print('broadcast', action, x, y)
    #     await self.send(text_data=json.dumps({'action': action, 'x': x, 'y': y}))

    async def receive(self, text_data):
        print('receive')
        text_data_json = json.loads(text_data)
        action = text_data_json['action']
        xline = text_data_json['xline']
        yline = text_data_json['yline']
        print('receive', action, xline, yline)
        await self.channel_layer.group_send(self.room_group_name, {'type': 'broadcast', 'action': action, 'xline': xline, 'yline': yline})

    async def broadcast(self, event):

        action = event['action']
        xline = event['xline']
        yline = event['yline']
        print('broadcast', action, xline, yline)
        await self.send(text_data=json.dumps({'action': action, 'xline': xline, 'yline': yline}))
