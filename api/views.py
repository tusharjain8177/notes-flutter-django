from rest_framework.decorators import api_view
from rest_framework.response import Response
from .Serializer import NoteSerializer
from .models import Notes


@api_view(["GET"])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Return an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Return an array of notes'
        },
        {
            'Endpoint': '/notes/create',
            'method': 'GET',
            'body': None,
            'description': 'Return an array of notes'
        },
        {
            'Endpoint': '/notes/delete',
            'method': 'GET',
            'body': None,
            'description': 'Return an array of notes'
        },
    ]

    return Response(routes)


@api_view(["GET"])
def getNotes(request):
    notes = Notes.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getNote(request, pk):
    note = Notes.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def createNotes(request):
    data = request.data

    note = Notes.objects.create(
        body=data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
def updateNotes(request, pk):
    data = request.data

    note = Notes.objects.get(id=pk)
    serializer = NoteSerializer(note, data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def deleteNotes(request, pk):
    note = Notes.objects.get(id=pk)
    note.delete()
    return Response('Note is deleted')




    
