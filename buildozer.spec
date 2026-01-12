[app]

# (str) Title of your application
title = MyApp

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"]([^'"]*)+['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,requests

# (str) Custom source folders for requirements
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

#
# author = © Copyright Info

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 1.9.1

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash animation using Lottie format.
# See https://lottie.github.io/lottie-docs/ for examples and https://airbnb.design/lottie/
# for general documentation.
# Lottie files can be created using various tools, like Adobe After Effects, Synfig, Blender.
#p4a.lottie = "path/to/lottie/file.json"

# (string) Presplash animation using Lottie format.
# This is a 24bit png presplash-1536x2048.png should be in the same folder as main.py
# See https://python-for-android.readthedocs.io/en/latest/buildoptions/#presplash
#p4a.presplash = "path/to/lottie/file.json"

# (list) Permissions
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,FOREGROUND_SERVICE

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# In past, was `android.arch` as we weren't supporting builds for multiple archs at the same time.
android.archs = arm64-v8a, armeabi-v7a

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android SDK version to use
#android.sdk = 23

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
# android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
# android.accept_sdk_license = False

# (str) The android NDK version to use
# android.ndk = 19c

# (str) The android SDK version to use
# Recommended value is "31" for android 12
# android.sdk = 31

# (str) The incremental version number, leave 0 to be set automatically
# android.incremental_storage_version = 0

# (str) The format of the apk file name (android only)
# Default: "myapp-%(version)s-%(build)s-%(package)s-%(arch)s.apk"
# android.apk_name_format = "%(package)s-%(fullname)s-%(arch)s-%(release)s-%(build)s.apk"

# (list) The Android shared libraries which will be added to the apk
#android.add_src =

# (list) The Android optional libraries which will be added to the apk
# The full list is available at
# https://python-for-android.readthedocs.io/en/latest/buildoptions/#add-jar
# and https://github.com/kivy/python-for-android/blob/master/pythonforandroid/recipes
# Possible values are:
# - all
# - kivy (default) includes all dependencies of kivy
# - plyer (default) includes plyer
# - audiostream, camera, curl, ffmpeg, ffpyplayer, freetype, harfbuzz, icu, iio,
#   jnius, netifaces, numpy, openssl, png, sdl2_image, sdl2_mixer, sdl2_ttf,
#   sqlite3, sdl2, webview, zbar
# - comma separated list, e.g: `requirements = kivy, plyer, openssl`
#android.whitelist = kivy, plyer

# (str) Bootstrap to use for android builds
# p4a.bootstrap = sdl2

# (int) Target Android API, should be as high as possible.
#android.api = 27

# (int) Minimum API your APK will support.
#android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 27

# (str) Android NDK version to use
#android.ndk = 19b

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
#android.add_src =

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will not be enabled
#android.ouya.category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
#android.manifest.intent_filters =

# (str) launchMode to set for the main activity
#android.manifest.launch_mode = standard

# (list) Android additional libraries to copy into libs/armeabi
#android.add_jars = libs/android/*.jar

# (bool) Indicate whether the screen should stay on
# Don't forget to add the WAKE_LOCK permission if you set this to True
#android.wakelock = False

# (list) Android application meta-data to set (key=value format)
#android.meta_data =

# (list) Android library project to add (will be added in the
# project.properties automatically.)
#android.library_references =

# (list) Android shared libraries which will be added to the classpath
#android.library_references =

# (list) Android java compilation options
# this can for example be necessary if you need to import java .lang classes.
# See "https://developer.android.com/reference/tools/javac-compiler-options"
# for valid options
# android.java_compiler_arguments =

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Android logcat only display log matching filters
#android.logcat_priority = 1

# (str) Android additional adb arguments
#android.adb_args = -H host -P 5037

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# In past, was `android.arch` as we weren't supporting builds for multiple archs at the same time.
#android.archs = arm64-v8a, armeabi-v7a

# (int) overrides automatic versionCode computation (used in build.gradle)
# this is not the same as app version and should only be edited if you know what you're doing
# android.numeric_version = 1

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) XML file for custom backup rules (see official auto backup documentation)
# android.backup_rules =

# (str) If you need to insert variables into your AndroidManifest.xml file,
# you can do so with the manifestPlaceholders property.
# This property takes a map of key-value pairs. (via a string)
# Usage example : android.manifest_placeholders = hsappId:my_hsapp_id,hsappId2:my_hsapp_id2
#android.manifest_placeholders =

# (str) If you need to insert variables into your strings.xml file,
# you can do so with the strings_placeholders property.
# This property takes a map of key-value pairs. (via a string)
# Usage example : android.strings_placeholders = app_name:My App Name
#android.strings_placeholders =

# (list) Permissions to add to AndroidManifest.xml.
#android.manifest_permissions = RECORD_AUDIO

# (list) Permissions to add to AndroidManifest.xml.
#android.manifest_permissions = RECORD_AUDIO

# (list) A list of application arguments to be passed to the Python script
#android.entrypoint = org.kivy.android.PythonActivity
#android.args = -O

# (bool) Preserve the java source code after jni folder processing to debug
#android.preserve_java_source = False

# (str) The format used to package the app for release mode (aab or apk).
# android.release_artifact = aab
android.release_artifact = apk

# (str) The format used to package the app for debug mode (apk or aab).
# android.debug_artifact = apk
android.debug_artifact = apk

#
# Python for android (p4a) specific
#

# (str) python-for-android fork to use, defaults to upstream (kivy)
#p4a.fork = kivy

# (str) python-for-android branch to use, defaults to master
#p4a.branch = master

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
#p4a.source_dir =

# (str) The directory in which python-for-android should look for your own build recipes (if any)
#p4a.local_recipes =

# (str) The directory in which python-for-android should look for your own build modules (if any)
#p4a.local_modules =

# (str) The directory in which python-for-android should build packages (if empty, it will be automatically set)
#p4a.build_dir =

# (int) The number of parallel build jobs. (default: 4)
#p4a.jobs = 4

# (str) The format used to package the app for debug mode (aab or apk).
#p4a.debug_artifact = apk

# (str) The format used to package the app for release mode (aab or apk).
#p4a.release_artifact = aab

#
# iOS specific
#

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios
# Alternately, specify the URL and branch of a git checkout:
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

# Another platform dependency: ios-deploy
# Uncomment to use a custom checkout
#ios.ios_deploy_dir = ../ios_deploy
# Or specify URL and branch
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.7.0

# (bool) Whether or not to sign the code
ios.codesign.allowed = false

# (str) Name of the certificate to use for signing the debug version
# Get a list of available identities: buildozer ios list_identities
#ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) The development team to use for signing the debug version
#ios.codesign.development_team.debug = <hexstring>

# (str) Name of the certificate to use for signing the release version
#ios.codesign.release = %(ios.codesign.debug)s

# (str) The development team to use for signing the release version
#ios.codesign.development_team.release = <hexstring>

# (str) URL pointing to .ipa file to be installed
# This option should be defined along with `display-image` and `full-size-image` options.
#ios.manifest.app_url =

# (str) URL pointing to an icon (57x57px) to be displayed during download
# This option should be defined along with `app-url` and `full-size-image` options.
#ios.manifest.display_image =

# (str) URL pointing to a large icon (512x512px) to be displayed during download
# This option should be defined along with `app-url` and `display-image` options.
#ios.manifest.full_size_image =

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
# bin_dir = ./bin

#    -----------------------------------------------------------------------------
#    List as sections
#
#    You can define all the "list" as [section:key].
#    Each line will be considered as a option to the list.
#    Let's take [app] / source.exclude_patterns.
#    Each line following this key will be added to the list.
#    Example:
#
#   [app:source.exclude_patterns]
#   patterns/spec*.spec
#   patterns/test_*.md
#
#    -----------------------------------------------------------------------------

#    -----------------------------------------------------------------------------
#    Profiles
#
#    You can extend section / key with a profile
#    For example, you want to deploy a demo version of your application without
#    HD content. You could first change the title to add "(demo)" in the name
#    and extend the excluded directories to remove the HD content.
#
#   [app@demo]
#   title = My Application (demo)
#
#   [app@demo:source.exclude_patterns]
#   images/hd/*
#
#    Then, invoke the command line with the "demo" profile:
#
#   buildozer --profile demo android debug
