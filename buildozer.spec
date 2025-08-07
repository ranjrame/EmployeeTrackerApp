
[app]
title = Employee Tracker
package.name = employeetracker
package.domain = org.hallimane
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = kivy
orientation = portrait
fullscreen = 1
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b
# Tell Buildozer to use custom SDK path
export ANDROIDSDK=$HOME/android-sdk
export ANDROIDNDK=$HOME/.buildozer/android/platform/android-ndk-r25b
export PATH=$ANDROIDSDK/platform-tools:$ANDROIDSDK/cmdline-tools/latest/bin:$PATH

[buildozer]
log_level = 2

