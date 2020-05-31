from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# from calculatorapp.logic.logic import SymPyGamma
import wolframalpha


def index(request):
    return render(request, 'index.html')


def input(request):
    if request.method == "GET":
        q = request.GET['query']

        # g = SymPyGamma()
        # r = g.eval(q)
        # r = eval(q)
        client = wolframalpha.Client('PL5HW2-Q2XGXA6RAV')
        try:
            res = client.query(q)
            try:
                pic = res['pod'][1]['subpod']['img']['@src']
            except:
                pic = res['pod'][1]['subpod'][1]['img']['@src']
        except KeyError:
            mydictionary = dict(title="Input", q=input, ans="Check that the data entry is correct", result=True)
        else:
            mydictionary = {
                "q": q,
                "ans": next(res.results).text,
                "pic": pic,
                "error": False,
                "result": True
            }

        return render(request, 'index.html', context=mydictionary)
