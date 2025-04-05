#!/bin/bash

# This script is for the author's personal use only!!
# This script is used to push images to GHCR
# You need to have a docker account and login to GHCR using the GHCR_TOKEN
# echo <GHCR_TOKEN> | docker login ghcr.io -u smars-bin-hu --password-stdin
# You need to have the images in your local, otherwise, uncomment the command that pull the images from docker hub

# set variables
SOURCE_PREFIX="smarsbhu/proj1-dwh-cluster"
TARGET_PREFIX="ghcr.io/smars-bin-hu/proj1-dwh-cluster"
TAG="smars-1.1.1"

IMAGES=(
  hadoop-master-smars-1.1.2
  hadoop-worker1-smars-1.1.2
  hadoop-worker2-smars-1.1.2
  mysql-hive-metastore-smars-1.1.2
  hive-smars-1.1.2
  spark-smars-1.1.1
  oracle-oltp-smars-1.1.1
  airflow-smars-1.1.1
)

for image in "${IMAGES[@]}"; do
#   pull image from docker hub if not exist in your local
#   echo "➡️  Pulling image: $SOURCE_PREFIX:$image"
#   docker pull $SOURCE_PREFIX:$image

#   tag image for ghcr
#   echo "🏷️  Tagging for GHCR: $TARGET_PREFIX:$image"
#   docker tag $SOURCE_PREFIX:$image $TARGET_PREFIX:$image

#   push image to ghcr
  echo "🚀 Pushing to GHCR: $TARGET_PREFIX:$image"
  docker push $TARGET_PREFIX:$image
done
