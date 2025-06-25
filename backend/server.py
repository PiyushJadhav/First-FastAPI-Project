from src.app import app

# if we are running this file directly, we can start the server
if __name__ == "__main__":
    import uvicorn
    # run on local host 
    uvicorn.run(app, host="0.0.0", port=8000, log_level="info")



    