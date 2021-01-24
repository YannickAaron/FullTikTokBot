## Project is still under construction

# FullTikTokBot

## Usage

1) download repo and go into folder
2) install
```bash
#mac
sh install.sh 
#linux
./ install.sh 
```
3) enjoy

## Architectures Supported (Host System)

The architectures (necessary for chromedriver) currently supported by this image are:

- `raspberry pi/aarch64` using `linux/aarch64` (armv7l)
- `mac:windows/x86_x64` using `linux/x64`

More will come in the future

## File Structure

/tiktokSleniumAPI #contains all files regarding the inofficial tiktok access  
__/crx contains browser plug-ins  
__/loginCookies contains the userdata for login  
__/seleniumDriver contains the chrome drivers for selenium  
  
/media contains all asstes for creating the videos including the finished files. 
__/downloads  
__/movie_asstets contains all additional files (e.g. sounds)  
__/readyForUpload contains the unused files  
__/usedFiles contains files that have been already uploaded  
__/cutted contains folder named reagrding to the videoID with all the cutted scenes  
  
/logs contains logs an screenshots  


/ubuntu-rasperry contains all Files concerning the port to rasperry  

