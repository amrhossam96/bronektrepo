from django.http import HttpResponse, JsonResponse
import json
from .serializers import ProfileModelSerializer, BroCodeSerializer
from  ...models  import Profile, Brocode


def response(request):
    
    profile = Profile.objects.get(user=request.user)
    serializer = ProfileModelSerializer(profile)
    return JsonResponse(serializer.data, safe=False)

def post_brocode(request):
    if(request.user.is_authenticated):
        brocode_body = json.loads(request.body)['brocode-body']
        brocode_author = request.user
        brocode = Brocode(author=brocode_author, brocode_body=brocode_body)
        brocode.save()
        serializer = BroCodeSerializer(brocode)
        response = serializer.data
        response['author'] = request.user.username
        response['author-display-name'] = request.user.profile.display_name
        return JsonResponse(response, safe=False)