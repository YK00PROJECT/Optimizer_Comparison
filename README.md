# README

## Overview
This repository contains code for comparing the performance of different optimizers in training a convolutional neural network (CNN) on the MNIST dataset. The optimizers considered in this analysis are Adam, RMSprop, Adadelta, Adagrad, and SGD.

## Requirements
- TensorFlow (v2.x)
- Matplotlib (for visualization)

## Instructions
1. **Importing Libraries**: First, import the necessary libraries including TensorFlow and Matplotlib.

2. **Importing Data**: Load the MNIST dataset using TensorFlow's built-in `mnist` module.

3. **Data Preprocessing**: Reshape the data and perform normalization. Also, convert the labels to categorical form.

4. **Build Optimizer Function**: Define a function `build_optimizer(op)` to create a CNN model with a specified optimizer. This function returns a compiled model.

5. **Compare Optimizer Performance**: Iterate through the list of optimizers, build a model for each optimizer, train it, and evaluate its performance. Print out the accuracy for each optimizer.

6. **Plotting Optimizer Accuracy**: Visualize the accuracy of each optimizer over epochs using Matplotlib.

## Results
- Adam and RMSprop performed the best in terms of accuracy and loss reduction, with Adam being slightly better.
- Adadelta performed poorly.
- Adagrad and SGD showed improvement over epochs but didn’t reach the same level of performance as Adam and RMSprop within the given epochs. 

## Conclusion
Based on this analysis, Adam and RMSprop are recommended optimizers for training CNNs on the MNIST dataset due to their superior performance. However, the choice of optimizer may vary depending on the specific characteristics of the dataset and the network architecture.
