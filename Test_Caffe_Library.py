# import necessary libraries
import cv2
import numpy as np
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# path to the Caffe prototxt file
prototxt = os.path.join(script_dir, 'colorization_deploy_v2.prototxt')
# path to the Caffe pre-trained model
model = os.path.join(script_dir, 'colorization_release_v2.caffemodel')
# path to a NumPy cluster center points file
points = os.path.join(script_dir, 'pts_in_hull.npy')

# Load the Caffe model
net = cv2.dnn.readNetFromCaffe(prototxt, model)
pts = np.load(points)
pts = pts.transpose().reshape(2, 313, 1, 1)
layer1 = net.getLayerId('class8_ab')
layer2 = net.getLayerId('conv8_313_rh')
net.getLayer(layer1).blobs = [pts.astype('float32')]
net.getLayer(layer2).blobs = [np.full([1, 313], 2.606, dtype='float32')]

def process_image(file_path):
    # read image from the path
    test_image = cv2.imread(file_path)
    # convert image into gray scale
    test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
    # convert image from gray scale to rgb format
    test_image = cv2.cvtColor(test_image, cv2.COLOR_GRAY2RGB)

    # normalise the image
    normalised = test_image.astype("float32") / 255.0
    # convert the image into LAB
    lab_image = cv2.cvtColor(normalised, cv2.COLOR_RGB2LAB)
    # resize the image
    resized = cv2.resize(lab_image, (224, 224))

    # extract the value of L for Lab image
    L = cv2.split(resized)[0]
    L -= 50

    # set the input
    net.setInput(cv2.dnn.blobFromImage(L))
    # find the values of a and b
    ab = net.forward()[0, :, :, :].transpose((1, 2, 0))
    # resize
    ab = cv2.resize(ab, (test_image.shape[1], test_image.shape[0]))

    L = cv2.split(lab_image)[0]
    # combining L, a, b
    Lab_coloured = np.concatenate((L[:, :, np.newaxis], ab), axis=2)

    # convert Lab image to RGB_colored
    RGB_coloured = cv2.cvtColor(Lab_coloured, cv2.COLOR_LAB2RGB)

    # limits the values in array
    RGB_coloured = np.clip(RGB_coloured, 0, 1)
    # change the pixel intensity back to [0,255]
    RGB_coloured = (255 * RGB_coloured).astype('uint8')

    # save the image in desired path
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads', 'coloured_image.jpg')
    cv2.imwrite(output_path, cv2.cvtColor(RGB_coloured, cv2.COLOR_RGB2BGR))
    
    return 'coloured_image.jpg'  # Return the name of the output file
