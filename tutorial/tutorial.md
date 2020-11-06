# Getting Started
This tutorial will show you how to create and run a Pachyderm pipeline that extracts and saves all frames from a video or a small collection of videos.

## Prerequisites
The **frames** pipeline was created and tested for a local installation of Pachyderm, and thus, it is recommended to use a local installation to run it.

To do so, follow the instructions for a [Local Installation of Pachyderm](https://docs.pachyderm.com/latest/getting_started/local_installation/).

### Versions used
A local installation of Pachyderm runs on minikube, which is a local Kubernetes cluster. This tutorial uses **minikube v1.14.2** and **Pachyderm v1.11.5**.

# 1) Gather Videos of Interest
For the purposes of testing this pipeline, collect a few short (less than 5 minutes in length) videos you would like to convert to frames.

> By default, the minikube cluster has a limited amount of memory (4000MB) and disk (20000MB) resources, so too many videos or videos that are too long can cause the cluster to fail. See the *TLS handshake timeout* section of the Troubleshooting document.

Public domain archives, such as the [Internet Archive](https://archive.org), are good sources for test videos.

**Recommendations**:
1. Place all of the videos in a single directory for easy access.
2. Name the video files in a command-line friendly way because all of the frames of a video will be extracted and saved to a directory named after the video filename.
    - For example: Use the filename `sample_newsclip_20201103.mp3` rather than `Sample Newsclip 20201103.mp3` because a directory named `sample_newsclip_2020_11_03` is cleaner and doesn't require spaces to be escaped when trying to access it from the command-line.
    - For more details on file naming practices, see [here](https://library.stanford.edu/research/data-management-services/data-best-practices/best-practices-file-naming).

# 2) Start Up Pachyderm (if not started already)
Start Minikube:
```
minikube start
```
Start Pachyderm:
```
pachctl deploy local
```

# 3) Create videos repo
Once Pachyderm is running (may take a few minutes), create the **videos** repo, which will contain all of the videos you'd like to process.
```
pachctl create repo videos
```

Confirm the creation of the repo.
```
pachctl list repo
```

> Be sure to name the **videos** repo exactly as such because the pipeline expects it as an input.

# 4) Add video files to the videos repo
With all of your videos stored on a local directory, you can add all of them to the **videos** repo by running:
```
pachctl put file -r videos@master:/ -f PATH_TO_VIDEOS_LOCAL_DIRECTORY
```

Otherwise, if you only have one video, or you want to add videos individually, you can do so by navigating to the directory of a video and running:
```
pachctl put file videos@master -f VIDEO_FILENAME
```

> You can also run:
> ```pachctl put file videos@master -h```
> in order to see different ways to add video files to the repo.

Verify that all videos of interest have been added.
```
pachctl list file videos@master
```

# 5) Create frames pipeline
Now that you have the videos to be processed checked into the **videos** repo, you can create the **frames** pipeline using the specification `frame-extract.json` defined in this GitHub repository.
```
pachctl create pipeline -f https://raw.githubusercontent.com/lfierro/pachyderm-vid2frames-demo/master/frame-extract.json
```

And, upon running the command, a job that executes the pipeline for the files in the **videos** repo will begin. You can see its status by running:
```
pachctl list job
```

> Note: It may take a few minutes for the job to appear.

# 6) Check pipeline output

## Listing Files
Once the job is completed, a new repo should be created called **frames** (which was named in the pipeline specification `frame-extract.json`). In it, should be a directory for each video.

You can check all of the files committed to the **frames** repo by first seeing all of the directories created.
```
pachctl list file frames@master
```

Then, you can list all of the frames in a directory. There will be many, so you may only want to see a preview of that list by piping the list command output to head.
```
pachctl list file frames@master:/SINGLE_VIDEO_DIRECTORY | head
```

## Viewing Frames
Now, you can view one of the frames. The command differs based on your operating system.

macOS before Catalina:
```
pachctl get file frames@master:/SINGLE_VIDEO_DIRECTORY/frame0.jpg | open -f -a /Applications/Preview.app
```

macOS Catalina:
```
pachctl get file frames@master:/SINGLE_VIDEO_DIRECTORY/frame0.jpg | open -f -a /System/Applications/Preview.app
```

Linux 64-bit:
```
pachctl get file frames@master:/SINGLE_VIDEO_DIRECTORY/frame0.jpg | display
```

# 7) Optional: Saving/exporting frames locally
If you would like to download all of the extracted frames in the **frames** repo, run:
```
pachctl get file frames@master:/ -ro LOCAL_PATH_TO_SAVE
```

# 8) Shutting down
Once you're ready to shut down Pachyderm. Simply run:
```
minikube delete
```

# Appendix
- The **frames** pipeline was tested using videos in MKV, mp4, and MOV format.
- The **frames** pipeline extracts frames based on a video's encoded frame rate, and each frame is saved as a JPEG.
- For more on the pipeline specification, see Pachyderm's [Pipeline Specification docs](https://docs.pachyderm.com/latest/reference/pipeline_spec/).
- This tutorial was created and run using macOS High Sierra.
