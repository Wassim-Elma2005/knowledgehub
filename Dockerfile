FROM ubuntu:22.04

# install dependencies
RUN apt-get update && apt-get install -y git python3 python3-pip

# set working directory
WORKDIR /app

# copy project files
COPY . .

# install python packages
RUN pip install -r requirements.txt

# run configuration
EXPOSE 8000
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]