# Django Portfolio Site

## Overview

This Django project is designed to create a personal portfolio site, employing the MVT (Model, View, Template) architecture. The portfolio showcases various job entries, each comprising an image, summary, description, and year. The site includes a homepage and a details page for each job.

## Models

### Job Model

- **image**: Image field
- **summary**: Char field (max length = 100)
- **description**: Char field (max length = 1000)
- **year**: Char field (max length = 4)

## Views

### Homepage

- Renders `home.html`
- Displays a profile photo, contact details, and clickable icons redirecting to respective job details.

### Details

- Renders `details.html`
- Displays the job description based on the job id (primary key).

## Templates

### home.html

- Contains a profile photo, contact details.
- Displays job details as clickable icons redirecting to respective job details.

### details.html

- Shows the job description based on the job id (primary key).

## Static Files

- Profile photo: `dinesh1.jpg`
- JS and CSS files for styling and interactivity.

## Media Files

- Job photos stored in the `images` folder.

## How to Run

1. Clone the repository: `git clone https://github.com/your-username/your-repo.git`
2. Navigate to the project directory: `cd your-repo`
3. Install dependencies: `pip install -r requirements.txt`
4. Apply migrations: `python manage.py migrate`
5. Create a superuser: `python manage.py createsuperuser`
6. Run the development server: `python manage.py runserver`
7. Access the site at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Feel free to customize the content, styling, and additional features to suit your personal portfolio needs.
