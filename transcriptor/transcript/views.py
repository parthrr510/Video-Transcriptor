from django.shortcuts import render
from .forms import URLForm
from .functions import convertToTranscript,getSummarization

def home(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            transcript,bool = convertToTranscript(url)
            if bool:
                summary = getSummarization(transcript)
            else:
                summary = transcript
            context = {
                'summ':summary
            }
            return render(request, 'transcript/output.html', context)

    else:
        form = URLForm()

    return render(request, 'transcript/main.html', {'form': form})