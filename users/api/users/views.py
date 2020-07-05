from django.http import HttpResponse, JsonResponse
import json
from .serializers import ProfileModelSerializer, BroCodeSerializer
from  ...models  import Profile, Brocode, Timeline, Following, Follower
import time, datetime

def response(request):
    
    profile = Profile.objects.get(user=request.user)
    serializer = ProfileModelSerializer(profile)
    return JsonResponse(serializer.data, safe=False)

def post_brocode(request):

    if(request.user.is_authenticated):
        brocode_body = json.loads(request.body)['brocode-body']
        brocode_author = request.user
        brocode = Brocode(author=brocode_author.profile, brocode_body=brocode_body)
        brocode.save()
        personal_timeline = Timeline.objects.get(owner=brocode_author.profile)
        personal_timeline.brocodes_list.add(Brocode.objects.get(id=brocode.id))
        followers_list = Follower.objects.get(profile=brocode_author.profile)
        followers_list = followers_list.followers.all()
        if(len(followers_list)>0):
            for follower in followers_list:
                target_timeline = Timeline.objects.get(owner=follower)
                target_timeline.brocodes_list.add(Brocode.objects.get(id=brocode.id))
        serializer = BroCodeSerializer(brocode)
        response = serializer.data
        response['author'] = request.user.username
        response['author-display-name'] = request.user.profile.display_name
        return JsonResponse(response, safe=False)

def get_brocodes(request, timestamp):
    if (request.method == "GET"):

        datetime_ = datetime.datetime.fromtimestamp(float(timestamp)/1000)
        personal_timeline = Timeline.objects.get(owner=request.user.profile)
        retrived_brocodes = personal_timeline.brocodes_list.all().order_by('-created').exclude(author=request.user.profile)[:30]
        filtered_brocodes = []
        for bc in retrived_brocodes:
            if(int(bc.created.timestamp()) > int(timestamp)):
                filtered_brocodes.append(bc)
        
        
        serializer = BroCodeSerializer(filtered_brocodes, many=True)
        for s in serializer.data:
            s['author'] = Brocode.objects.get(id=s['id']).author.user.username
            s['author-display-name'] = Brocode.objects.get(id=s['id']).author.display_name
        return JsonResponse(serializer.data,safe=False)

def like_brocode(request, brocode_id):
    brocode = Brocode.objects.get(id=brocode_id)
    brocode.likes +=1
    serializer = BroCodeSerializer(brocode)
    return JsonResponse(serializer.data,safe=False)

def unlike_brocode(request, brocode_id):
    brocode = Brocode.objects.get(id=brocode_id)
    brocode.likes -=1
    serializer = BroCodeSerializer(brocode)
    return JsonResponse(serializer.data,safe=False)


def search_users(request):
    search_query = json.loads(request.body)['search-query']
    profiles = Profile.objects.filter(display_name__startswith=search_query)
    serializer = ProfileModelSerializer(profiles,many=True)
    return JsonResponse(serializer.data,safe=False)


def get_profile(request,slug):
    print(slug)
    user = Profile.objects.get(slug=slug)
    serializer = ProfileModelSerializer(user)
    response = serializer.data
    response['username'] = user.user.username
    print(response)
    return JsonResponse(response,safe=False)

def commit_follow(request,slug):
    sender_profile = request.user.profile
    receiver_profile = Profile.objects.get(slug=slug)
    following_list = Following.objects.get(profile=sender_profile)
    following_list.follows.add(receiver_profile)
    followers_list = Follower.objects.get(profile=receiver_profile)
    followers_list.followers.add(sender_profile)
    response = {"message":"Success"}
    return JsonResponse(json.dumps(response),safe=False)