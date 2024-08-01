FROM python:3.12
EXPOSE 5000

# Configure Poetry
ENV POETRY_VERSION=1.8.3
# RUN pip install poetry==${POETRY_VERSION}
RUN pip install "poetry==$POETRY_VERSION" && \
    poetry config virtualenvs.create false
		
WORKDIR /app

# Install dependencies
COPY ./pyproject.toml ./poetry.lock /app/
RUN poetry install

# # Run your app
COPY . /app/
CMD [ "poetry", "run", "flask", "--app", "wonder_lust_ml/hello", "run", "--host", "0.0.0.0"]