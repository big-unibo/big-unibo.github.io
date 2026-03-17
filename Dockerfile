FROM ruby:4.0
RUN mkdir /materials
COPY Gemfile* /materials/
WORKDIR /materials
RUN gem install bundler
RUN bundler install
COPY . /materials
CMD ["sh", "./build.sh"]