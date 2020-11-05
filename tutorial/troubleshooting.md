# Troubleshooting
This document contains issues that may be encountered while running the **frames** pipeline.

# TLS handshake timeout
Sometimes, when running a pachctl command, you may receive a "TLS handshake timeout" response.

Check the status of minikube by running:
```
minikube status
```

If you see that the apiserver has a status of **stopped**, it is likely minikube has run out of resources (see [https://github.com/kubernetes/minikube/issues/3649](https://github.com/kubernetes/minikube/issues/3649)), and/or you are not running the most recent version of minikube.

## Solution
- Upgrade minikube OR
- Increase Memory and Disk amounts for minikube cluster

# Job failure
If the pipeline job fails, run:
```
pachctl logs --job=JOB_ID
```

With the JOBID pulled from:
```
pachctl list job
```

# Can't find folder of frames for a video file
This likely means that the video format was not readable by OpenCV. You can verify by running:
```
pachctl list job
```

Then:
```
pachctl logs --job=JOB_ID
```

If you see the printed message, 'Video VIDEO_FILENAME could not be read. Please check file format.' then that video wasn't properly read by OpenCV.
