##!/bin/sh
#
#if [ ! "$UWSGI_MODULE" ]; then
#    UWSGI_MODULE="loki.wsgi:app"
#fi
#
#if [ ! "$UWSGI_MASTER" ]; then
#    UWSGI_MASTER=1
#fi
#
#if [ ! "$UWSGI_HTTP" ]; then
#    UWSGI_HTTP=0.0.0.0:8080
#fi
#
#if [ ! "$UWSGI_PROCESSES" ]; then
#    UWSGI_PROCESSES=16
#fi
#
#if [ ! "$UWSGI_THREADS" ]; then
#    UWSGI_THREADS=8
#fi
#
#export UWSGI_MODULE UWSGI_MASTER UWSGI_HTTP UWSGI_PROCESSES UWSGI_THREADS
#
#exec "$@"