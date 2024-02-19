from rest_framework import serializers

from course.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


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

    # class Meta:
    #     model = Course
    #     fields = '__all__'




