
# YouTube Manager

## Overview
YouTube Manager is a command-line application that allows users to manage a collection of YouTube video entries. The application supports basic CRUD (Create, Read, Update, Delete) operations and is implemented using three different storage solutions: files (JSON), SQLite3, and MongoDB.

## Features
- List all YouTube videos
- Add a new YouTube video
- Update details of an existing YouTube video
- Delete a YouTube video
- Exit the application

## Requirements
- Python 3.x
- `pymongo` library (for MongoDB implementation)
- SQLite3 (for SQLite implementation)

## Installation

### MongoDB Implementation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/youtube-manager.git
   cd youtube-manager
   ```

2. **Install dependencies**:
   ```bash
   pip install pymongo
   ```

3. **Ensure MongoDB is running**:
   ```bash
   mongod
   ```

4. **Run the application**:
   ```bash
   python youtube_manager_mongodb.py
   ```

### SQLite3 Implementation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/youtube-manager.git
   cd youtube-manager
   ```

2. **Run the application**:
   ```bash
   python youtube_manager_sqlite.py
   ```

### Files (JSON) Implementation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/youtube-manager.git
   cd youtube-manager
   ```

2. **Run the application**:
   ```bash
   python youtube_manager_files.py
   ```

## Usage

1. **Start the application**:
   ```bash
   python youtube_manager_<implementation>.py
   ```

2. **Follow the on-screen menu to manage YouTube videos**:
   - `1`: List all YouTube videos
   - `2`: Add a new YouTube video
   - `3`: Update an existing YouTube video's details
   - `4`: Delete a YouTube video
   - `5`: Exit the application

## Notes
- Ensure MongoDB is properly installed and running before starting the MongoDB implementation.
- The file-based implementation uses `youtube.txt` to store data in JSON format.


