# Professional Portfolio Website

A professional Streamlit portfolio website showcasing your resume, projects, and contact information.

## Features

- **Landing Page**: Visually engaging introduction with profile photo and career highlights
- **Resume Section**: Clean layout of education, experience, skills, and certifications
- **Projects Section**: Showcase of projects with descriptions, technologies, and outcomes
- **Contact Section**: Links to professional profiles and a contact form
- **Responsive Design**: Looks great on all devices
- **Easy to Update**: Simple structure for quick content updates

## Setup Instructions

1. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

2. Add your personal content:
   - Place your profile photo in `assets/profile_photo.jpg`
   - Place your resume PDF in `assets/resume.pdf`
   - Update the personal information in `app.py`

3. Run the application:
   ```
   streamlit run app.py
   ```

## Customization

### Personal Information
Update the following sections in `app.py` to personalize your portfolio:

- Your name, professional title, and introduction in the `display_home()` function
- Education details in the `display_resume()` function
- Work experience in the `display_resume()` function
- Skills in the `display_resume()` function
- Project details in the `display_projects()` function
- Contact information in the sidebar and `display_contact()` function

### Styling
Customize the appearance by modifying the CSS in the `local_css()` function.

## Project Structure

```
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── README.md           # Documentation
└── assets/             # Directory for images and documents
    ├── profile_photo.jpg  # Your profile photo
    └── resume.pdf         # Your resume in PDF format
```

## Adding Projects

To add a new project, copy one of the existing project templates in the `display_projects()` function and update the:

1. Project title
2. Description
3. Technologies used
4. Key outcomes
5. Project links
6. Project image

## Contact

Update the contact information in both the sidebar and the contact section to reflect your actual contact details.