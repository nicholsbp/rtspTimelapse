
Capture timelapse images from an RTSP stream using python and opencv. Requires python and opencv. Configure with your RTSP url and preferred capture interval.

When you are done capturing, you can assemble the images into a video using ffmpeg like so
```
ffmpeg -framerate 30 -pattern_type glob -i '*.jpg' -c:v libx264 -r 30 -pix_fmt yuv420p output.mp4
```
