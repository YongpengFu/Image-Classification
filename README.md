# Image-Classification
This is a school project to process images using conventional machine learning and deep learning techniques.

This project focused on building a customized web scraping tool to download thousands of images from Amazon and creating a model that could accurately classify the products in the images. Our team implemented various conventional machine learning techniques, including logistic regression, k-nearest neighbors, support vector machine, Gaussian Naïve Bayes, trees (multiple models), and random forest, as well as neural networks such as MLP and CNN, to classify 11 different products. We also explored the effects of using dimensionality reduction for image classification.

Some achievement we got at the end of this project:

- We built our own customized web scraping tool to download thousands of images from Amazon for a range of human wearable products, including Earbuds, VR sets, Fitness trackers, Hearing Aids, Watches, Sunglasses, and Hats.
- The following questions are answered as well:
  - How do conventional machine learning techniques compare to neural networks for image analysis and classification? We saw that the neural networks here didnt perform as well as random forest, but with work, we might be able to get a cnn predictor that could get a higher accuracy. The random forest classifier achieved a result of 76% accuracy. While CNN didn't perform as well as we had hoped, but there is still the potential to continue working on and improving the model. One of the challenges of CNN is how long it takes to train the model compared to random forest, where runtimes are in hours instead of seconds or minutes.
  - What are the effects of using dimensionality reduction for image classification? We saw that the runtime for training models was reduced, and for random forest, not much accuracy was sacrificed either.
  - Can we come to a final best-suited model to tag images for human wearable products? Our random forest predictor preformed the best of any of the models.
