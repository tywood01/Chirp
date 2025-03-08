from django.test import TestCase
from django.contrib.auth.models import User
from chirper.models import Chirp, Profile, Likes, Follow


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


# Create your tests here.
class TestChirperViews(TestCase):
    def test_profile(self):
        pass

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
