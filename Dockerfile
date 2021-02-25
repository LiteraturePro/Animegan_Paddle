# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.6.12-slim

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN apt update && apt install -y \
    libgl1-mesa-glx \
    libglib2.0-dev \
    libgomp1

# Install production dependencies.
RUN pip install -r requirements.txt

# CPU
RUN pip install paddlehub==2.0.0
RUN pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple

# Model
RUN hub install animegan_v1_hayao_60
RUN hub install animegan_v2_hayao_64
RUN hub install animegan_v2_hayao_99
RUN hub install animegan_v2_paprika_74
RUN hub install animegan_v2_paprika_97
RUN hub install animegan_v2_paprika_98
RUN hub install animegan_v2_shinkai_33
RUN hub install animegan_v2_shinkai_53

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind 0.0.0.0:8080 --workers 1 --threads 8 --timeout 0 app:app
#CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 app:app