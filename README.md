# Content Moderation: Text, Image, and Video

This repository contains code for content moderation, including text, image, and video moderation. It utilizes various libraries for different moderation tasks.

## Features

### 1. Text Moderation
- Utilizes the `better_profanity` library to censor profane language in text.
- Implements a function to censor profanity from given text.

### 2. Image Moderation
- Uses the `nudenet` library for detecting nudity in images.
- Provides a script to detect nudity in a given image file.
- Processes image frames extracted from videos for nudity detection.

### 3. Video Moderation
- Processes video frames for nudity detection using the `nudenet` library.
- Flags videos containing nudity based on the number of detections in frames.
