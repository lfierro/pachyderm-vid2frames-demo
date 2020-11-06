# Troubleshooting
This document contains issues that may be encountered while running the **frames** Pachyderm pipeline.

# TLS handshake timeout
Sometimes, when running a `pachctl` command, you may receive a `TLS handshake timeout` response.

Check the status of minikube by running:
```
minikube status
```

If you see that the apiserver has a status of `stopped`, it is likely minikube has run out of resources (see [this issue](https://github.com/kubernetes/minikube/issues/3649)), and/or you are not running the most recent version of minikube.

## Solution
- Upgrade minikube OR
- Increase memory and disk amounts for your minikube cluster

# Job failure
If the pipeline job fails, run:
```
pachctl logs --job=JOB_ID
```

With the JOBID pulled from:
```
pachctl list job
```

# Video file produces an empty folder in the frames repo
This means that the video format was not readable by OpenCV. You can verify by running:
```
pachctl list job
```

Then:
```
pachctl logs --job=JOB_ID
```

You should see the message, `Video VIDEO_FILENAME could not be read. Please check file format.` in the logs.

## Solution
Update the format of the video file. mp4, MKV, and MOV have historically worked well.

Then, delete the old file from the **videos** repo and its corresponding folder in the **frames** repo by running:
```
pachctl delete file videos@master:/FAILED_VIDEO_FILENAME
```

You can then add the updated file to the **videos** repo.
```
pachctl put file videos@master -f UPDATED_VIDEO_FILENAME
```

And, the **frames** pipeline should immediately begin to process the updated video file.
