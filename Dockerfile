FROM python:3.12.3-alpine


#docker build . --build-arg APP_VERSION=0.1.0
ARG APP_VERSION=0.1.0
ARG APP_NAME=hello
ENV APP_DIST=$APP_NAME-$APP_VERSION.tar.gz

WORKDIR /app
COPY dist/$APP_DIST /app/

RUN pip3 install $APP_DIST
RUN rm $APP_DIST

CMD "python3" "-m" "cinema"