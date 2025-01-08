from rest_framework import generics, status
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Task
from .serializers import TaskSerializer


class TaskCreateListView(generics.ListCreateAPIView):
    """
    User Task creation and listing view
    """

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        try:
            return Task.objects.filter(user=self.request.user)
        except Exception:
            raise ValidationError(
                {"error": "Unable to fetch tasks. Please try again later."}
            )

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except ValidationError as e:
            raise ValidationError(
                {"error": "Invalid data provided.", "details": str(e)}
            )
        except Exception:
            raise ValidationError(
                {"error": "Task creation failed. Please try again later."}
            )


class TaskUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    User Task Update and Deletion view
    """

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_object(self):
        try:
            obj = super().get_object()
            if obj.user != self.request.user:
                raise NotFound("Task not found")
            return obj
        except Task.DoesNotExist:
            raise NotFound({"error": "The requested task does not exist"})
        except Exception as e:
            raise ValidationError(
                {
                    "error": "An error occurred while retrieving the task.",
                    "details": str(e),
                }
            )

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except ValidationError as e:
            return Response(
                {"error": "Validation error occurred.", "details": e.detail},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            return Response(
                {
                    "error": "An error occurred while updating the task.",
                    "details": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def destroy(self, request, *args, **kwargs):
        try:
            task = self.get_object()
            task.delete()
            return Response(
                {"message": "Task deleted successfully."}, status=status.HTTP_200_OK
            )
        except Task.DoesNotExist:
            return Response(
                {"error": "The task does not exist."}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {
                    "error": "An error occurred while deleting the task.",
                    "details": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
