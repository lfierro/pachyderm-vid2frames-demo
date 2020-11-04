# Overview
This repository contains materials to run a Pachyderm pipeline that extracts frames from a video and saves them as stills.

- frame-extract.py: Python script that executes the video to image extraction
- frame-extract.json: Pipeline specification to run video to image extraction using a Pachyderm pipeline job
- Dockerfile: Dockerfile used to create images(s) in DockerHub repository *lfierro/pachyderm-vid2frames-demo*
  - includes the building of libraries needed for video processing with OpenCV v4.4.0
- Tutorial: folder containing:
  - tutorial.md - a walkthrough of how to use and run the files above
  - troubleshooting.md - some issues that may emerge and recommended fixes
