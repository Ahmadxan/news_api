from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Commit, Category, Article
from rest_framework.exceptions import NotFound
from .serializers import CategorySerializer, CommitSerializer, ArticleSerializer
from rest_framework.response import Response


class CategoryViewSets(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryView(APIView):

    def get_object(self, pk):
        try:
            model = Category.objects.get(id=pk)
            return model
        except Exception:
            raise NotFound("Model not found!")

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            category = self.get_object(kwargs.get('pk'))
            serializer = CategorySerializer(category, many=False)
        else:
            category = Category.objects.all()
            serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        model = self.get_object(kwargs.get('pk'))
        serializer = CategorySerializer(data=request.data, instance=model)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        model = self.get_object(kwargs.get('pk'))
        model.delete()
        return Response({"deleted": "state"})


class ArticleViewSets(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleView(APIView):

    def get_object(self, pk):
        try:
            model = Article.objects.get(id=pk)
            return model
        except Exception:
            raise NotFound('Article Not Found!')

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            article = self.get_object(kwargs.get('pk'))
            serializer = ArticleSerializer(article, many=False)
        else:
            articles = Article.objects.all()
            serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        model = self.get_object(kwargs.get('pk'))
        serializer = ArticleSerializer(data=request.data, instance=model)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, **kwargs):
        model = self.get_object(kwargs.get('pk'))
        model.delete()
        return Response({"state": 'deleted'})


class CommitView(APIView):

    def get_object(self, pk):
        try:
            model = Commit.objects.get(id=pk)
            return model
        except Exception:
            raise NotFound("Commit not found!")

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            commit = self.get_object(kwargs.get('pk'))
            serializer = CommitSerializer(commit, many=False)
        else:
            commits = Commit.objects.all()
            serializer = CommitSerializer(commits, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CommitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        model = self.get_object(kwargs.get('pk'))
        serializer = CommitSerializer(data=request.data, instance=model)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, **kwargs):
        model = self.get_object(kwargs.get('pk'))
        model.delete()
        return Response({"state": 'deleted'})


class CommitViewSets(ModelViewSet):
    queryset = Commit.objects.all()
    serializer_class = CommitSerializer