#!/bin/bash
sudo apt install ansible -y
ansible-galaxy collection install ansible.posix 
ansible-galaxy collection install openstack.cloud
ansible-galaxy collection install community.general
ansible-galaxy collection install community.Kubernetes
ansible-galaxy collection install kubernetes.core
python3 -m pip install openshift==0.11.2
