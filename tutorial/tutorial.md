# Getting Started
This tutorial will show you how to create and run a Pachyderm pipeline that extracts and saves all frames from a video or collection of videos.

## Prerequisites
The *frames* pipeline (see *frame-extract.json* for pipeline naming) was created and tested for a local installation of Pachyderm, and thus, it is recommended to use a local installation to run it.

To do so, follow instructions for a [Local Installation of Pachyderm](https://docs.pachyderm.com/latest/getting_started/local_installation/)

### Versions used
This tutorial uses Minikube v1.14.2 and Pachyderm v1.11.5.

## Gather Videos of Interest
Collect the videos you would like to convert to frames.

For the purposes of testing, public domain archives are good sources for videos.

**Recommendations**:
1. Place all of the videos in a single folder for easy access
2. Name the video files in a directory-friendly way - all of the frames of a video are extracted and saved to a folder named after the video filename
  - For example: use the filename "sample_newsclip_2020_11_03.mp3" rather than "Sample Newsclip 2020_11_03.mp3"

# Start Up Pachyderm (if not started already)
Start Minikube:
```
minikube start
```
Start Pachyderm:
```
pachctl deploy local
```

# Create videos repo
Once Pachyderm is running (may take a few minutes), create the *videos* repo, which will contain all of the videos you'd like to process.
```
pachctl create repo videos
```

Confirm the creation of the repo.
```
pachctl list repo
```

Be sure to name the *videos* repo exactly as such because the *frames* pipeline expects it as an input.

# Add video files to the videos repo
With all of your videos stored on a local folder, you can add all of them to the video repo by running:
```
pachctl put file -r videos@master:/ -f PATH_TO_VIDEOS_LOCAL_FOLDER
```

Verify that all videos of interest have been added.
```
pachctl list file videos@master
```

# Create frames pipeline
Now that you have videos to be processed checked into the *videos* repo, you can create the *frames* pipeline.
```
pachctl create pipeline -f https://raw.githubusercontent.com/lfierro/pachyderm-vid2frames-demo/master/frame-extract.json
```

This command uses the pipeline specification *frame-extract.json* defined in this GitHub repository.

And, upon running this command, a job that executes the pipeline for the videos in the *videos* repo will begin. You can see its status by running:
```
pachctl list job
```

Note: It may take a few minutes for the job to appear.

# Check pipeline output
Once the job is completed, a new repo should be created called *frames*. In it, should be a directory for each video.

You can check all of the files committed to the *frames* repo by first seeing all of the directories created.
```
pachctl list file frames@master
```

Then, you can list all of the frames in a directory. There will be many, so you may only want to see a preview of that list by piping the list command to head.
```
pachctl list file frames@master:/SINGLE_VIDEO_DIRECTORY | head
```

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

# Saving/exporting frames locally
?is this possible?

# Wrapping Up
Once everything is completed, and you'd like to shut down Pachyderm. Simply run:
```
minikube delete
```
