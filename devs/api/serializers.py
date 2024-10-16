from rest_framework import serializers
from projects.models import Project, Tag, Review
from users.models import Profile


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProjectsSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False)
    tag = TagSerializer(many=True)
    reviews = serializers.SerializerMethodField()

    """Review is another model. To get all reviews:"""
    def get_reviews(self, project):
        reviews = project.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data

    class Meta:
        model = Project
        fields = '__all__'
