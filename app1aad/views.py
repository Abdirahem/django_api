
from turtle import title
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import BlogSerializer
from . models import Blog


@api_view(["GET"])
def getRoutes(request):
    routes = [
        {
            "id": 3,
            "title": "why somali don not work",
            "body": "I have a feeling too. Oh honey, he's teasing you, nobody has two television sets. You're gonna break his arm. Biff, leave him alone. Let him go. Let him go. Hello, Jennifer"
        },
        {
            "id": 4,
            "title": "why somali don not work",
            "body": "I have a feeling too. Oh honey, he's teasing you, nobody has two television sets. You're gonna break his arm. Biff, leave him alone. Let him go. Let him go. Hello, Jennifer"
        },
        {
            "id": 5,
            "title": "why somali don not work",
            "body": "I have a feeling too. Oh honey, he's teasing you, nobody has two television sets. You're gonna break his arm. Biff, leave him alone. Let him go. Let him go. Hello, Jennifer"
        },
        {
            "id": 6,
            "title": "why somali don not work",
            "body": "I have a feeling too. Oh honey, he's teasing you, nobody has two television sets. You're gonna break his arm. Biff, leave him alone. Let him go. Let him go. Hello, Jennifer"
        },
    ]

    return Response(routes)


@api_view(['GET'])
def getPosts(request):
    posts = Blog.objects.all()
    serializer = BlogSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPost(request, pk):
    posts = Blog.objects.get(id=pk)
    serializer = BlogSerializer(posts, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createPost(request):
    data = request.data
    posts = Blog.objects.create(
        title=data['title'],
        content=data['content']
    )
    serializer = BlogSerializer(posts, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updatePost(request, pk):
    data = request.data
    posts = Blog.objects.get(id=pk)
    serializer = BlogSerializer(posts, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deletePost(request, pk):
    post = Blog.objects.get(id=pk)
    post.delete()
    return Response("Record is deleted")
