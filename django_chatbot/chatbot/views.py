from django.shortcuts import render
from django.http import JsonResponse
from bardapi import Bard
import os
os.environ["_BARD_API_KEY"] = "cggP5kYz-hYq3KUQtAEPAGBbd2HcXtWO5Fq6CywP51aH90hvarfoAnBoLQ4TC_6OWg7gUw."

def ask_bard(message):
    answer = Bard().get_answer(str(message))['content']
    return answer

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_bard(message)
        return JsonResponse({'message':message,'response':response})
    else:
        return render(request,'chatbot.html')