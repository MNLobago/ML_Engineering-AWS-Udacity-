## Project 2: MNIST Digits Classification

### Overview

In this project, we build and train a model to classify handwritten digits from the MNIST dataset using PyTorch. The project demonstrates the end-to-end process of data preprocessing, model training, evaluation, and deployment.

### Files

- **MNIST-digits.ipynb**: This Jupyter Notebook contains the complete code for data preprocessing, model training, evaluation, and results visualization.
- **MNIST-digits.html**: A static HTML version of the Jupyter Notebook for easy viewing.
- **requirements.txt**: This file contains a list of all the dependencies required to run the notebook.

### Setup

To set up the environment and run the notebook, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/MNLobago/ML_Engineering-AWS-Udacity-.git
    cd ML_Engineering-AWS-Udacity-
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Jupyter Notebook:**

    ```bash
    jupyter notebook MNIST-digits.ipynb
    ```

### Dependencies

The project requires the following libraries, which are listed in the `requirements.txt` file:

- opencv-python-headless==4.5.3.56
- matplotlib==3.4.3
- numpy==1.21.2
- pillow==7.0.0
- bokeh==2.1.1
- torch==1.11.0
- torchvision==0.12.0
- tqdm==4.63.0
- ipywidgets==7.7.0
- livelossplot==0