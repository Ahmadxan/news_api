from rest_framework import serializers
from .models import Article, Category, Commit


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance

    # class Meta:
    #     model = Category
    #     fields = '__all__'


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category_id = serializers.IntegerField()
    author_id = serializers.IntegerField()
    title = serializers.CharField()
    body = serializers.CharField()
    image = serializers.ImageField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.author_id = validated_data.get('author_id', instance.author_id)
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.image = validated_data.get('image', instance.image)

    # class Meta:
    #     model = Article
    #     fields = '__all__'


class CommitSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField()
    article = serializers.IntegerField()
    email = serializers.EmailField()
    text = serializers.CharField()

    def create(self, validated_data):
        return Commit.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('title', instance.author)
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.email = validated_data.get('email', instance.email)
        instance.body = validated_data.get('body', instance.body)

    # class Meta:
    #     model = Commit
    #     fields = '__all__'
