---
comments: true
date: 2006-05-16 19:19:37
layout: post
slug: accesing-ntfs-and-fat32-partiton-on-ubuntu
title: Accesing NTFS and FAT32 partiton on Ubuntu
wordpress_id: 92
---


NTFS and FAT32 are the partitions used by windows to access them from UBUNTU follow these For NTFS just type open terminal and type 

    sudo fdisk -l

then see which partition is of NTFS (i am taking it as  /dev/hda1) then to mount it to /media/windows type

    sudo mkdir /media/windows
    sudo cp /etc/fstab /etc/fsab_backup
    sudo gedit /etc/fstab

add the following at the end of the file

    /dev/hda1    /media/windows ntfs  nls=utf8,umask=0222 0    0

save the file then in terminal type

    sudo mount -a

For FAT32 partition just repeat the above with different type

    /dev/hda1    /media/windows vfat  iocharset=utf8,umask=000  0    0

Make sure u name the folders differently for FAT32 and NTFS and also change the text to be copied accordingly

