# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM paddlepaddle/paddle:2.0.0

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN apt update && apt install -y \
    libgl1-mesa-glx \
    libglib2.0-dev

# Install production dependencies.
RUN pip install -r requirements.txt

# CPU
# RUN pip install paddlehub==2.0.0
# RUN pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind 0.0.0.0:8080 --workers 1 --threads 8 --timeout 0 app:app
# CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 app:app