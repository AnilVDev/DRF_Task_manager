import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from task.models import Task


# Fixture to create a test user
@pytest.fixture
def create_test_user():
    user = get_user_model().objects.create_user(
        email="testuser@example.com",
        password="testpassword123",
        first_name="Test",
        last_name="User",
    )
    return user


@pytest.fixture
def api_client():
    return APIClient()


# Fixture to create a task
@pytest.fixture
def create_test_task(create_test_user):
    return Task.objects.create(
        user=create_test_user,
        title="Test Task",
        description="Task for testing purposes",
        status="pending",
    )


# Test TaskCreateListView
@pytest.mark.django_db
def test_create_task_view(api_client, create_test_user):
    api_client.force_authenticate(create_test_user)
    data = {
        "title": "New Task",
        "description": "Description of the new task",
        "status": "pending",
    }
    response = api_client.post(reverse("task-list"), data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Task.objects.filter(title="New Task").exists()


@pytest.mark.django_db
def test_list_tasks_view(api_client, create_test_user, create_test_task):
    api_client.force_authenticate(create_test_user)
    response = api_client.get(reverse("task-list"))
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1


@pytest.mark.django_db
def test_update_task_view(api_client, create_test_user, create_test_task):
    api_client.force_authenticate(create_test_user)
    data = {
        "title": "Updated Task",
        "description": "Updated description",
        "status": "in_progress",
    }
    response = api_client.put(
        reverse("task-detail", kwargs={"pk": create_test_task.id}), data
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == "Updated Task"


@pytest.mark.django_db
def test_delete_task_view(api_client, create_test_user, create_test_task):
    api_client.force_authenticate(create_test_user)
    response = api_client.delete(
        reverse("task-detail", kwargs={"pk": create_test_task.id})
    )
    assert response.status_code == status.HTTP_200_OK
    assert not Task.objects.filter(id=create_test_task.id).exists()


# Test cases for TaskUpdateDeleteView
@pytest.mark.django_db
def test_retrieve_task_view(api_client, create_test_user, create_test_task):
    api_client.force_authenticate(create_test_user)
    response = api_client.get(
        reverse("task-detail", kwargs={"pk": create_test_task.id})
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == create_test_task.title


@pytest.mark.django_db
def test_update_task_view_fail(api_client, create_test_user, create_test_task):
    api_client.force_authenticate(create_test_user)
    data = {"title": "", "description": "", "status": "pending"}
    response = api_client.put(
        reverse("task-detail", kwargs={"pk": create_test_task.id}), data
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
