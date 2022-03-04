from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'info/index.html')

def about(reqeust):
    context = {'member':
                [
                    {'name':'Yeonseo Park', 'role':'칵테일 정보 기능', 'githubid':'YSPARK525', 'email':None},
                    {'name':'HaeSeong Yang', 'role':'회원가입 기능', 'githubid':'yanghs6', 'email':'yanghs632@gmail.com'},
                    {'name':'Yeongjun Lee',  'role':'커뮤니티 게시판 기능', 'githubid':'gotitgitgit', 'email':None}
                ]
              }
    
    # return render(reqeust, 'about.html', context)
    return render(reqeust, 'info/about.html', context)
