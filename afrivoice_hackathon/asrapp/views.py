
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .whisper_utils import transcribe_audio

def upload_audio(request):
    if request.method == 'POST' and request.FILES.get('audio_file'):
        audio_file = request.FILES['audio_file']
        fs = FileSystemStorage()
        filename = fs.save(audio_file.name, audio_file)
        file_path = fs.path(filename)
        transcription = transcribe_audio(file_path)
        return render(request, 'result.html', {{ 'transcription': transcription }})
    return render(request, 'upload.html')
