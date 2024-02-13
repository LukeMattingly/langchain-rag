Use this to run a local file-upload server.

# Setup

- Install dependencies with `pip install -r requirements.txt`
- Start the server with `python app.py`
- In the `pdf` project, find the `.env` file and change the `UPLOAD_URL` line to the following: `UPLOAD_URL=http://localhost:8050`
- Restart the PDF project
