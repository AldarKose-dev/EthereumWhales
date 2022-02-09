from django.shortcuts import render, redirect
from chartapp.parser import parser


def index(request):
    balances, accounts = parser()

    context = {
        "balances": balances,
        "accounts": accounts
    }
    return render(request, 'chartapp/index.html', context)
