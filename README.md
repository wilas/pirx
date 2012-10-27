# Description

`pirx`:

Small, fast and easy to use bash script, for renaming multiple files (photos, music, movies - depend filtr file exension) in a folder at once.

Useful for:
- change large batch of photos with names such as "DSC_1234.JPG" "IMG_0123.jpg" to give more convenient name.
- quickly and easily rename your music collection
- replace spaces with give character in multiple files in a folder

Good to know:
- Default filtr=.jpg|.JPG|.jpeg|.JPEG|.png|.PNG|.mp3|.awk|.mobi
- Sort entries alphabetically if not -t.

`pirx-fotodater`:

Set Modified Time to Date and Time Picture was Taken all [jpg|JPG|jpeg|JPEG] files in current directory

require: exiv2 (rhel/centos/sl: yum install exiv2)


## Install
    cp pirx* /usr/local/bin
    chmod +x pirx*

## Help
    pirx -h
    pirx-fotodater -h

## Usage examples (useful information):

List of files in directory:
    
    cmd: ls -la
        aaa.jpg
        bbb.jpg
        ccc.JPG
        ddd.avi

Change name all filtr files in directory:
    
    cmd: pirx -v roadtrip
    cmd: ls -la
        roadtrip00001.jpg
        roadtrip00002.jpg
        roadtrip00003.JPG
        ddd.avi

Change name all filtr files in directory and set output extension for files:
    
    cmd: pirx -v poland -o jpg
    cmd: ls -la
        roadtrip00001.jpg
        roadtrip00002.jpg
        roadtrip00003.jpg
        ddd.avi

