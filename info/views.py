from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'info/index.html')

def about(reqeust):
    context = {'member':
                [
                    {'name':'YeonSeo Park', 'role':['칵테일 정보', '일러스트 제작'], 'githubid':'YSPARK525', 'email':None},
                    {'name':'HaeSeong Yang', 'role':['배포', '회원가입', ], 'githubid':'yanghs6', 'email':'yanghs632@gmail.com'},
                    {'name':'YeongJun Lee',  'role':['커뮤니티 게시판', '회원가입'], 'githubid':'gotitgitgit', 'email':None}
                ]
              }
    
    return render(reqeust, 'info/about.html', context)
