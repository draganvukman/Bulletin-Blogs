from app import create_app

app = create_app()

# run the app
if __name__ == '__main__':
    app.run(debug=True)
