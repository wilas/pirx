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
        DSC0001 123.jpg
        DSC0002 122.jpg
        DSC1234 145.JPG
        simple.avi
        simple2.AVI

    cmd: ls -lat
        DSC0001 123.jpg
        DSC1234 145.JPG
        DSC0002 122.jpg
        simple2.AVI
        simple.avi

Change name all filtr files in directory:
    
    cmd: pirx -v roadtrip
    cmd: ls -la
        roadtrip00001.jpg
        roadtrip00002.jpg
        roadtrip00003.JPG
        simple.avi
        simple2.AVI

Change name all filtr files in directory sort by modification time:
    
    cmd: pirx -vt roadtrip
    cmd: ls -la
        roadtrip00001.jpg
        roadtrip00002.JPG
        roadtrip00003.jpg
        simple.avi
        simple2.AVI

Change name all filtr files in directory and set output file extension:
    
    cmd: pirx -v roadtrip -o jpg
    cmd: ls -la
        roadtrip00001.jpg
        roadtrip00002.jpg
        roadtrip00003.jpg
        simple.avi
        simple2.AVI

Change name all filtr files in directory and set extra input file extension:
    
    cmd: pirx -v roadtrip -i avi
    cmd: ls -la
        roadtrip00001.jpg
        roadtrip00002.jpg
        roadtrip00003.jpg
        roadtrip00004.avi
        simple2.AVI

Change name all filtr files in directory match pattern with extra input and output file extension:
    
    cmd: pirx -v -i avi|.AVI -p simple -o avi roadtrip
    cmd: ls -la
        DSC0001 123.jpg
        DSC0002 122.jpg
        DSC1234 145.JPG
        roadtrip00001.avi
        roadtrip00002.avi

Replace spaces in all filtr files in directory:

    cmd: pirx -vb _
    cmd: ls -la
        DSC0001_123.jpg
        DSC0002_122.jpg
        DSC1234_145.JPG
        simple.avi
        simple2.AVI

