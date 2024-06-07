# Google Image Scraper

## Project Overview

Google Image Scraper is a web application that allows users to easily fetch images from Google based on their search queries. The fetched images are stored in the WB format in a MongoDB database. 

## Features

- Simple user interface where users can type the search query for images they want.
- Backend fetches images from Google based on the search query.
- Stores fetched images in MongoDB.
- Hosted on Microsoft Azure as a web app.

## Technologies Used

- **Frontend**: HTML, CSS
- **Backend**: Flask
- **Database**: MongoDB
- **Hosting**: Microsoft Azure

## Workflow

1. **User Input**: User enters the search query for the desired images.
2. **Image Fetching**: The backend fetches images from Google based on the user's query.
3. **Storage**: Fetched images are stored in MongoDB in the WB format.

## How to Set Up This Project

1. **Install Requirements**: 
   - Ensure you have Python installed.
   - Install required packages by running:
     ```sh
     pip install -r requirements.txt
     ```
2. **Configure Database**:
   - Update the MongoDB database connection link in the code with your own MongoDB connection string.

3. **Run the Application**:
   - Start the application by running:
     ```sh
     python application.py
     ```

## Contributing

This project is open-source and free to use. Contributions and modifications are welcome. Feel free to fork the repository and make your changes.

## License

This project is licensed under the MIT License. You are free to use and modify the project as you please.

---

For any issues or questions, please contact the project maintainer.

Enjoy using the Google Image Scraper!