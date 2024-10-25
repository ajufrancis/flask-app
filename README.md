# Animal Selector and File Upload Flask Application

A simple web application built with Flask that allows users to select an animal (cat, dog, or elephant) and upload a file. The app displays the selected animal's image and provides details about the uploaded file.

# Features

- **Animal Selection:** Choose between a cat, dog, or elephant to display its image.
- **File Upload:** Upload any file to see its name, size, and type.
- **Simultaneous Actions:** Select an animal and upload a file at the same time.
- **User-Friendly Interface:** Built with HTML, CSS, and JavaScript for a smooth user experience.


# Project Files 

- **app.py:** The main Flask application file.
- **templates/index.html:** The HTML template for rendering the web page.
- **static/css/styles.css:** Optional CSS file for styling.
- **static/images/:** Folder containing images of the animals.
- **uploads/:** Directory to store uploaded files.
- **README.md:** Documentation file.
- **LICENSE:** License information for the project.


# Prerequisites

- Python 3.x
- Flask: Install via `pip install Flask`

# Installation

1. **Clone the Repository**
```
git clone https://github.com/your_username/your_repository.git
cd your_repository
```
2. **Set Up a Virtual Environment (Optional but Recommended)**
```
python3 -m venv venv
source venv/bin/activate
```
3. **Install Dependencies**
```
pip install Flask
```
4. **Add Animal Images**

  Place cat.jpg, dog.jpg, and elephant.jpg in the static/images/ directory.

# Usage
1. Run the Application
```
python app.py
```
2. **Access the Web Interface**
Open your web browser and navigate to `http://127.0.0.1:5000/`

3. **Interact with the Application**
   - **Select an Animal:** Choose an animal using the radio buttons and click Submit to display its image.
   - **Upload a File:** Use the file input to select a file and click Submit to view its details.
   - **Both:** You can select an animal and upload a file simultaneously.

   
