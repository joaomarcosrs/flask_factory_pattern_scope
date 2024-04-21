from app import create_app as application

app = application()

if __name__ == '__main__':
    # run in production
    app.run()
