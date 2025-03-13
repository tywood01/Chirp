"""
tests.py

Authors: Tytus Woodburn
Email: tytus.woodburn@student.cune.edu
Github: https://github.com/tywood01

Purpose:
    Provide integration tests for the chirper app.

"""

from django.test import TestCase
from django.contrib.auth.models import User
from chirper.models import Chirp, Profile, Likes, Follow
from django.urls import reverse


class TestChirperModels(TestCase):
    def test_add_chirp(self):
        user = User.objects.create_user(username="user", password="password")
        parent = Chirp.objects.create(
            body="parent content", date="2020-12-31 00:00:00", user=user
        )

        chirp = Chirp(
            body="content",
            user=user,
            parent=parent,
        )

        chirp.full_clean()
        chirp.save()
        chirp.refresh_from_db()

        self.assertEqual(chirp.body, "content")
        self.assertIsNotNone(chirp.date)
        self.assertEqual(chirp.user, user)
        self.assertEqual(chirp.parent, parent)

    def test_add_profile(self):
        pass

    def test_add_like(self):
        pass

    def test_add_follow(self):
        pass


class TestChirperViews(TestCase):
    def test_profile(self):
        user = User.objects.create_user(username="testuser", password="password")
        Profile.objects.create(user=user, bio="Test bio")

        Chirp.objects.create(body="Test chirp", user=user)

        # Log in as user
        self.client.login(username="testuser", password="password")

        # Get the profile page
        response = self.client.get(
            reverse("chirper:profile", kwargs={"username": "testuser"})
        )

        # Check that we get a 200 response
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Test bio")
        self.assertContains(response, "Test chirp")

        # TODO: Fix forms so that a user cannot follow themselves.
        # self.assertNotContains(response, "Unfollow")
        # self.assertNotContains(response, "Follow")

    def test_my_profile(self):
        pass

    def test_chirps(self):
        pass

    def test_add_chirp(self):
        pass

    def test_toggle_like(self):
        pass

    def test_toggle_follow(self):
        pass
