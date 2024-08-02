# Railway Enquiry System

This project is a web-based Railway Enquiry System built using Django. It allows users to check various railway-related information like PNR status, station details, and train schedules.

<img src="https://github.com/user-attachments/assets/88298577-4735-4810-af49-d0230701d626" alt="Image 7" width="275"/>
<img src="https://github.com/user-attachments/assets/19919d5d-5fd0-4d0d-9329-33cc2409d82e" alt="Image 8" width="300"/>
<img src="https://github.com/user-attachments/assets/440b24cc-dd1a-4303-bb53-c7387907eb1d" alt="Image 9" width="200"/>
<img src="https://github.com/user-attachments/assets/6602c089-73f5-4b8b-a690-aa1f8bbe9a71" alt="Image 10" width="150"/>

## Project Structure

- **RailwayEnquirySystem/**: The main directory for the project.
  - `db.sqlite3`: SQLite database file.
  - `manage.py`: Django management script.
  - **pages/**: Contains HTML templates for the web application.
    - `about.html`
    - `head.html`
    - `index.html`
    - `pnr-result.html`
    - `pnr.html`
    - `search-result.html`
    - `search.html`
    - `station-results.html`
    - `station.html`
    - `test.html`
  - **RailwayEnquirySystem/**: Django project directory.
    - `asgi.py`
    - `settings.py`
    - `urls.py`
    - `views.py`
    - `wsgi.py`
    - `__init__.py`
    - `__pycache__/`: Compiled Python files.
  - **s-files/**: Static files for the web application.
    - **css/**: Contains CSS files.
      - `pnr_status.css`
      - `templatemo_style1.css`
    - **images/**: Contains images used in the web application.
      - `indianrailwayimage.JPG`
      - `r.jpg`
      - `rail_logo_new_red.gif`
      - `templatemo_banner.jpg`
      - `templatemo_body_bg.jpg`
      - `templatemo_body_bg_2.jpg`
      - `templatemo_button_01.jpg`
      - `templatemo_button_02.jpg`
      - `templatemo_container_bg.png`
      - `templatemo_content_top.jpg`
      - `templatemo_footer.jpg`
      - `templatemo_h2_left.jpg`
      - `templatemo_h2_left_02.jpg`
      - `templatemo_h2_right.jpg`
      - `templatemo_h2_right_02.jpg`
      - `templatemo_image_01.jpg`
      - `templatemo_image_02.jpg`
      - `templatemo_image_03.jpg`
      - `templatemo_image_04.jpg`
      - `templatemo_main_column_section_bottom.jpg`
      - `templatemo_side_column_box_bottom.jpg`
      - `train.jpg`
    - **images4/**: Contains additional images.
      - Same image files as in the `images` directory.
    - `PR.pdf`: PDF file related to the project.
  - `test.py`: Script for testing.

## How to Run

1. **Install Dependencies:**
   - Ensure you have Python and Django installed.
   - Install the required Python packages:
     ```bash
     pip install -r requirements.txt
     ```

2. **Run the Django Server:**
   - Navigate to the project directory and run the Django server:
     ```bash
     python manage.py runserver
     ```
   - Access the web application at `http://127.0.0.1:8000/`.

3. **Database:**
   - The project uses an SQLite database (`db.sqlite3`).
   - If needed, migrate the database:
     ```bash
     python manage.py migrate
     ```

## Features

- **PNR Status Check:** Users can check the status of their PNR.
- **Station Details:** Provides information about different railway stations.
- **Train Schedules:** Users can search for train schedules and other details.
- **Responsive Design:** The web application is designed to be responsive and user-friendly.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Acknowledgements

- Thanks to the developers of Django for providing an excellent framework.
- Thanks to the creators of the templates and images used in this project.

## Contact

For any inquiries & issues, please contact [Subhajit Gorai](mailto:sg_outlp@outlook.com). I will resolve it in the same day..
