#!/usr/bin/env bash

# setup static ip address when connect use cable


# install vim
sudo apt-get -y update
sudo apt-get -y install vim

# install spf13-vim
curl https://j.mp/spf13-vim3 -L > spf13-vim.sh && sh spf13-vim.sh

# Install TightVNC
sudo apt-get -y install tightvncserver

# Setup git. Default set to my github account
git config --global user.email "shaokexu@gmail.com"
git config --global user.name "shaoke"



