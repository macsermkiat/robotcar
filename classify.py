# import the necessary packages
from keras.applications import ResNet50
#from keras.applications import InceptionV3
#from keras.applications import Xception # TensorFlow ONLY
#from keras.applications import VGG16
#from keras.applications import VGG19
#from keras.applications import inception_resnet_v2 
from keras.applications import imagenet_utils
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
import numpy as np
#import cv2
import h5py

def classify(): 
  inputShape = (224, 224)
  preprocess = imagenet_utils.preprocess_input
  model = ResNet50(weights="imagenet")
  image_path = 'ship.jpg'
  image = load_img('ship.jpg', target_size=(224,224))
  image = img_to_array(image)
  image = np.expand_dims(image, axis=0)
  image = preprocess(image)

  # classify the image
  preds = model.predict(image)
  P = imagenet_utils.decode_predictions(preds)
  # loop over the predictions and display the rank-5 predictions +
  # probabilities to our terminal

  for (i, (imagenetID, label, prob)) in enumerate(P[0]):
        output = ("{}. {}: {:.2f}%".format(i + 1, label, prob * 100))
        print(output)


