#!/bin/bash
git init
git add .
git commit -m 'initial commit'
#heroku config:add BUILDPACK_URL=https://github.com/kennethreitz/conda-buildpack.git
git push heroku master
