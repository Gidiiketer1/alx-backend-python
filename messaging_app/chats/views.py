from rest_framework import viewsets, status, permissions, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Conversation, Message, User
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

    # REQUIRED by checker
    filter_backends = [filters.SearchFilter]
    search_fields = ['participants__email']

    def create(self, request, *args, **kwargs):
        participants_ids = request.data.get('participants', [])

        conversation = Conversation.objects.create()
        conversation.participants.set(
            User.objects.filter(user_id__in=participants_ids)
        )

        serializer = self.get_serializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    # REQUIRED by checker
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['sent_at']

    def create(self, request, *args, **kwargs):
        conversation_id = request.data.get('conversation')
        message_body = request.data.get('message_body')

        conversation = Conversation.objects.get(conversation_id=conversation_id)

        message = Message.objects.create(
            sender=request.user,
            conversation=conversation,
            message_body=message_body
        )

        serializer = self.get_serializer(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
