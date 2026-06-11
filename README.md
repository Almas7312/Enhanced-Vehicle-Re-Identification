# Enhanced-Vehicle-Re-Identification

## Overview

Enhanced Vehicle Re-Identification is a computer vision system developed for identifying and tracking vehicles across surveillance cameras.

The system combines:

* YOLOv3 Vehicle Detection
* Siamese Neural Network based Vehicle Re-Identification
* Structural Similarity (SSIM)
* Color Histogram Matching
* Django Web Application
* MySQL Database

The project detects vehicles from uploaded surveillance videos and identifies vehicles that match a given reference image.

## Features

* Vehicle Detection
* Vehicle Tracking
* Vehicle Re-Identification
* Multi-camera Surveillance Support
* Vehicle Image Storage
* Admin Dashboard
* Camera Management
* Vehicle Search

## Technologies

* Python
* OpenCV
* TensorFlow
* Keras
* YOLOv3
* Django
* MySQL

## Vehicle Classes

The system detects:

* Car
* Bus
* Truck

using YOLOv3 trained on COCO Dataset.

## Workflow

1. Upload surveillance video
2. Detect vehicles using YOLOv3
3. Extract vehicle crops
4. Store detected vehicles
5. Compare with query image
6. Compute:

   * Siamese Similarity
   * Color Similarity
   * Structural Similarity
7. Return matching vehicles

## Results

The system successfully identifies vehicles across different frames and camera viewpoints while maintaining high matching accuracy.

## Future Scope

* Smart City Integration
* Real-Time Vehicle Tracking
* License Plate Recognition
* Multi-Camera Vehicle Search
* Cloud Deployment
