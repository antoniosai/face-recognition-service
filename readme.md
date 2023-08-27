# Face Recognition Service
A Stateless Service/ Application that allows you to check if the both of images is similar or not by just sending through HTTP Form Data. Built with [Python 3.8](https://www.python.org/downloads/release/python-380/), [Flask 2.3.3](https://flask.palletsprojects.com/en/2.3.x/), [Face Recognition](https://pypi.org/project/face-recognition/)

## Pull Docker Image

    docker pull antoniosai/face-recognition-service:latest

## Run with Docker

    docker run -p 5000:5000 antoniosai/face-recognition-service:latest

After running command above. You can access it directly through Postman or just with Your own Application.

***Method: [POST] http://localhost:5000/compare***

    form-data: {
	    image: your image location. This must contain file (jpg, png),
	    url: url location to be compared. Just URL string
    }

![Example 1: How to Use It](https://raw.githubusercontent.com/antoniosai/face-recognition-service/master/screenshot/screenshot-1.png)

### With cURL 

    curl -X POST -F "url=https://example.com/image.jpg" -F "image=@/path/to/image1.jpg" http://localhost:5000/compare

## License

This Project is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).