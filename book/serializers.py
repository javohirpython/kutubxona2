from rest_framework.serializers import ModelSerializer
from .models import Book, Category, Author

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ('__all__')

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')

class BookSerializer(ModelSerializer):
    author = AuthorSerializer()
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = ('__all__')


