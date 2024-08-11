# Railway Enquiry System

This project is a web-based Railway Enquiry System built using Django. It allows users to check various railway-related information like PNR status, station details, and train schedules.

<img width="300" alt="1" src="https://github.com/user-attachments/assets/ed64dde5-82d4-4f7c-8c60-ee4b8c95063e">
<img width="300" alt="2" src="https://github.com/user-attachments/assets/4cabab81-927a-4630-90c1-b44a6f4b4b5c">
<img width="300" alt="3" src="https://github.com/user-attachments/assets/600f059a-24ae-4773-8767-bcff70d3ad04">
<img width="300" alt="4" src="https://github.com/user-attachments/assets/bc7806f1-b67f-4e2f-83d1-578866752997">
<img width="300" alt="5" src="https://github.com/user-attachments/assets/fd9e6bef-cb68-4208-98f8-11cb3a8b44c9">

## Project Structure

- **RailwayEnquirySystem/**: The main directory for the project.
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
