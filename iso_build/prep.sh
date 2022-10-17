#!/bin/bash
sudo dnf copr enable dwrobel/pykickstart -y
sudo dnf copr enable dwrobel/livecd-tools -y
sudo dnf install -y mock pykickstart livecd-tools
sudo usermod -a -G mock $USER
