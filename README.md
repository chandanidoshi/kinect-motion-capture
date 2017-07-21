# Kinect Motion Capture

## Motivation
The motivation for our project was that using motion capture can make the animation of the character extremely realistic, and also provides a significant amount of aid to the animator. By using motion capture, one can get a more accurate representation of a character in a much easier and more efficient way.

## Implementation
Using the Kinect for Windows SDK v1.0, we were able to detect the 20 joints of a human skeleton at 30 frames per second, record them in a CSV file. Then, in Maya, we wrote a Python script to read the csv file and create keyframes at each time step, which animated our skeleton joint system perfectly. We rigged a model to the skeleton, and were able to animate our figure in time. More information on this can be found in our write-up. 

## Video
The example of our project can be found <a href="https://www.youtube.com/watch?v=H7Ow2yNyVAA"> here </a>.

## Collaborators
Evan Denmark and Chandani Doshi

