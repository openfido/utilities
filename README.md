# About

This repository is intended to be a centralized hub of reusable code and script snippets, best 
used to help keep your code neat and DRY!

As this code is intended for reuse across numerous pipelines, be very careful when working on any scripts or code snippets, and always keep in mind the ideals of backwards compatibility. This repository should also be accessible across pipeline developers to pull standardized configuration blocks.

# Using Scripts 

Using a script or pre-built, common configurations from this repository is intended to be simple. You can copy and
paste the code snippet below into your openfido.sh file wherever you need to initialize the configuration, and thats it.

```
# install wget to download any remote configurations
apt-get -q -y install wget > /dev/null

# adjust the two lines below to remotely pull whichever configuration you want to run
wget https://raw.githubusercontent.com/openfido/utilities/main/openfidodl.sh
. ./openfidodl.sh
```

The code example above will download and run a script which accomplishes the following things for you:
1) installs nodejs
2) downloads a node codeblock
3) runs the node codeblock, which scans input files for download urls and outputs them in a text file
4) downloads all files from the urls into the input folder for use in your pipeline

All scripts should maintain this simple, easy-to-call format. 

# Configuration Development Rules

All additions to the utilities repository should be submitted via pull request and reviewed prior to merging. 

Your best effort should be made to maintain the structure of this repository, due to the nature of its use.

Complexity in configuration should be abstracted from the pipeline developers. Your script should be able to operate as a standalone element, which can pull and fulfill all dependencies it may rely on for its intended use.

Make good comments on your code and scripts. You may not need them now... but they are vital to maintaining your code! Knowing even just the intent of your code goes a long way if something breaks in the future.

TODO: Review and refine the utilities development rules. 