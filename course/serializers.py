from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from course.models import Course, Lesson, Subscription
from course.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('title', 'image', "description", 'url', 'course', 'owner')
        validators = [UrlValidator(field="url")]


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(source='lesson_set', many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('title', 'image', "description", 'lesson', 'lesson_count')

    def get_lesson_count(self, instance):
        if instance.lesson_set.all().first():
            return instance.lesson_set.all().count()
        return 0


class SubscriptionSerializer(serializers.ModelSerializer):
    is_subscribe = SerializerMethodField()

    def get_is_subscribe(self, obj):
        user = self.context['request'].user

        for sub in Subscription.objects.filter(user=user, course=obj.pk):
            for user in obj.user.all():
                if sub.user == user:
                    return True
            return False

    class Meta:
        model = Subscription
        fields = '__all__'
