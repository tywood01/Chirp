## Welcome to Chirper!

This project is a message posting service similar to X (Twitter) made for practice!

### Prerequisites

To run this project locally, you will need the following:

- **Git**: Version/source control
- **UV**: Virtual environment manager for Python

### Installation

To install this project, clone the repository and run the following commands:

```bash
git clone <repository url>
uv sync
uv run manage.py makemigrations
uv run manage.py migrate
uv run manage.py runserver
```
### Features

From there, you can make an account and start making chirps! (Someday, I hope to have this as a hosted service for fun!)

From the home page, you can browse public chirps and people's profiles. When logged in, you can like a post, follow someone, reply, or create new chirps!

### Code

There's also a collection of unit tests that utilize Django's built-in testing tool.

    ### Example Test

    Here is an example of a unit test for adding a chirp:

    ```python
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
    ```


### Future Ideas

- Utilize [Bandit](https://github.com/PyCQA/bandit) for security
- Use [Playwright](https://playwright.dev/docs/intro) for end-to-end testing
