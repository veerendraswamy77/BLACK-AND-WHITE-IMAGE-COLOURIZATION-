# BLACK-AND-WHITE-IMAGE-COLOURIZATION
This project presents an automated colorization system for black-and-white images using a deep learning
approach. Leveraging a U-Net convolutional neural network, the model predicts color channels from grayscale
inputs, delivering realistic and visually appealing results. By preserving the original image content and
structure, the system provides a reliable solution for restoring and enhancing monochrome images, with
potential applications in historical photo restoration, media production, and creative design. 


INTRODUCTION
Image colorization is a complex and challenging task that involves adding colour to grayscale
images, often with limited or ambiguous information. Traditional colorization techniques were
manual, relying on human intervention to select appropriate colours. Over time, automated
methods have emerged, including rule-based approaches and, more recently, machine learning
models that attempt to predict colours based on patterns in the data.
With the advent of deep learning, methods for image colorization have significantly evolved.
Convolutional Neural Networks (CNNs) and more specialized architectures, such as U-Net and
Generative Adversarial Networks (GANs), have shown promise in generating realistic
colorizations for grayscale images. The U-Net model, initially designed for biomedical image
segmentation, has been successfully adapted for other image-to-image tasks, including
colorization (e.g., [Ronneberger et al., 2015]). U-Net’s encoder-decoder structure with skip
connections allows it to capture fine details necessary for high-quality colour restoration.
Previous work, such as Zhang et al. (2016), leveraged CNN-based approaches to predict the
chrominance channels in the LAB colour space. GANs, as used in [Isola et al., 2017], have also
shown the ability to produce convincing colorized outputs by learning to create realistic colour
distributions. However, these models often require extensive training data and computational
resources. 

OBJECTIVES
 Develop a Deep Learning-Based Image Colorization Mode
Design and implement a U-Net-based neural network to predict the color components (AB
channels) of grayscale images in the LAB color space.
 Utilize the CIFAR-10 Dataset for Model Training and Evaluation
Train the model on a well-known dataset of natural images (CIFAR-10) to learn effective
colorization techniques for low-resolution (32x32 pixel) images.
 Preprocess Images for Efficient Learning
 Convert RGB images to LAB color space to separate luminance (L) from chrominance
(AB), simplifying the color prediction task.
 Quantitatively Evaluate Model Performance
Use the Structural Similarity Index (SSIM) to assess the perceptual and structural similarity
between the colorized output and the original images.
 Qualitatively Analyse Colorization Results
Visualize the colorized outputs and compare them against original color images to assess the
model's ability to generate realistic and vibrant colors. 
