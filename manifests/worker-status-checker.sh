#!/bin/bash


if sudo lsof | grep 10250 ;then
	echo "worker has already joined the cluster"
else
     sudo /tmp/join-command.sh
fi


