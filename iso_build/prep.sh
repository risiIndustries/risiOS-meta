#!/bin/bash
dnf copr enable dwrobel/pykickstart -y
dnf copr enable dwrobel/livecd-tools -y
sudo dnf install -y mock pykickstart livecd-tools
sudo usermod -a -G mock $USER
