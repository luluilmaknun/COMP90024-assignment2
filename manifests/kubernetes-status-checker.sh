#!/bin/bash
check=1
rm -rf checking.txt
while [ $check != 0 ]
do
  kubectl get pods 2&> checking.txt
  if cat checking.txt | grep "did you specify the right host or port"; then
        sleep 60
        check=$check+1
        if [ $check -eq 3 ]; then
	      exit 1
	fi
  else
        check=0
	rm -rf checking.txt
        echo "kubernetes cluster is ready"
  fi
done

