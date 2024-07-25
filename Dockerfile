FROM ruby:3.3
RUN mkdir /materials
COPY Gemfile* /materials/
WORKDIR /materials
RUN gem install bundler
RUN bundler install
COPY . /materials
CMD ["sh", "./build.sh"]