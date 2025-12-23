[app]

# App name shown on device
title = Message Deferral

# Package name (no spaces, lowercase)
package.name = messagedeferral

# Java-style domain (does not need to exist)
package.domain = org.messagedeferral

# Source code location
source.dir = .

# Files to include
source.include_exts = py,kv,png,jpg

# Main app file
entrypoint = main.py

# Kivy + Python only
requirements = python3,kivy

# App version
version = 0.1.0

# Screen orientation
orientation = portrait

# Fullscreen off (feels more utility-like)
fullscreen = 0

# Android SDK / NDK
android.api = 34
android.minapi = 21
android.ndk = 25b

# Architecture (modern phones)
android.archs = arm64-v8a,armeabi-v7a

# Permissions (INTENTIONALLY EMPTY)
android.permissions =

# Disable dangerous stuff
android.allow_backup = False

# Keep logs off in release builds
log_level = 1
