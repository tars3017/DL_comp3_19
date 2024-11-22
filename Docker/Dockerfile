FROM tensorflow/tensorflow:2.9.1-gpu-jupyter

RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx && \
    apt-get clean
RUN pip install matplotlib pandas scikit-learn tqdm numba opencv-python cryptography wandb notebook

RUN git clone https://github.com/deepsense-ai/roi-pooling.git &&\
	cd roi-pooling &&\
	python setup.py install
