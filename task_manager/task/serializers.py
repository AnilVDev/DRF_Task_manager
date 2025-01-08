from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "user",
            "title",
            "description",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["user", "created_at", "update_at"]

    def validate_title(self, value):
        """
        Validate that the title is unique for the authenticated user.
        """
        try:
            request = self.context.get("request")
            user = request.user if request else None

            if user:
                task_id = self.instance.id if self.instance else None
                existing_task = (
                    Task.objects.filter(user=user, title=value)
                    .exclude(id=task_id)
                    .first()
                )

                if existing_task:
                    raise serializers.ValidationError(
                        "A task with this title already exists for the user."
                    )
        except Exception as e:
            raise serializers.ValidationError(
                {"error": "An error occurred during validation.", "details": str(e)}
            )

        return value
