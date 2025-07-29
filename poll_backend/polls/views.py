from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from .models import Poll, Option
from .serializers import PollSerializer

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def create(self, request):
        data = request.data
        options_data = data.pop('options')
        poll = Poll.objects.create(**data)
        for option in options_data:
            Option.objects.create(poll=poll, **option)
        serializer = PollSerializer(poll)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def vote(self, request, pk=None):
        try:
            poll = Poll.objects.get(pk=pk)

            # Check if poll has expired
            if poll.expires_at and timezone.now() > poll.expires_at:
                return Response({'error': 'Voting period has ended.'}, status=status.HTTP_403_FORBIDDEN)

            option_id = request.data['option_id']
            option = Option.objects.get(id=option_id, poll_id=pk)
            option.votes += 1
            option.save()
            return Response({'status': 'vote recorded'})

        except Poll.DoesNotExist:
            return Response({'error': 'Poll not found'}, status=status.HTTP_404_NOT_FOUND)
        except Option.DoesNotExist:
            return Response({'error': 'Invalid option'}, status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response({'error': 'option_id is required'}, status=status.HTTP_400_BAD_REQUEST)
