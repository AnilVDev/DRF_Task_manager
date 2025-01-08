import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from user.models import CustomUser


# Example fixture for creating a test user
@pytest.fixture
@pytest.mark.django_db
def create_test_user():
    return CustomUser.objects.create_user(
        email="testuser@example.com",
        first_name="Test",
        last_name="User",
        password="testpassword123",
    )


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_user_registration(api_client):
    data = {
        "email": "newuser@example.com",
        "first_name": "New",
        "last_name": "User",
        "password": "newpassword123",
        "password_confirmation": "newpassword123",
    }

    response = api_client.post(reverse("register"), data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["message"] == "User successfully registered!"


@pytest.mark.django_db
def test_user_login(api_client, create_test_user):
    login_data = {"email": "testuser@example.com", "password": "testpassword123"}
    url = reverse("login")
    response = api_client.post(url, login_data)
    assert response.status_code == status.HTTP_200_OK
    assert "access_token" in response.data
    assert "refresh_token" in response.data


@pytest.mark.django_db
def test_invalid_user_login(api_client, create_test_user):
    invalid_login_data = {"email": "wronguser@example.com", "password": "wrongpassword"}
    response = api_client.post(reverse("login"), invalid_login_data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
