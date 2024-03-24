# Data Generator with Cohere

Data Generator App with Cohere API

## Overview

Are you struggling with not enough data to train your model? This app is for you! This app generates data for you using the Cohere API. You can generate data for text classification, text generation, and text summarization tasks. You can also generate data for multiple languages.

## Getting Started

### Environment Setup

To get started, create a virtual environment and activate it:

```bash
virtualenv venv
source venv/bin/activate
```

Create a local environment file (`.env`) and add your huggingface API key:

```bash
COHERE_API=your_cohere_api_key
```

### Install Dependencies

Next, install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### Run the Application

Now, you can run the application:

```bash
gradio app.py
```

This will start the application, allowing you to start generate your data.

## Usage

Once the application is up and running, you can interact with the generator through a web interface.

## Additional Resources

- Check out the chatbot on [![Hugging Face Spaces](https://img.shields.io/badge/🤗%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/mca183/data-generation-cohere)
