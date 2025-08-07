[app]
title = Employee Tracker
package.name = employeetracker
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,pandas
orientation = portrait
osx.kivy_version = 2.3.0
# (Inside buildozer.spec)
android.ndk = 25b
android.api = 33
android.sdk = 24
android.accept_sdk_license = True


[buildozer]
log_level = 2
warn_on_root = 1

[app.android]
# Add this to your buildozer.spec under [app] section
android.sdk_path = /home/runner/work/EmployeeTrackerApp/android-sdk

android.ndk_path = /home/runner/work/EmployeeTrackerApp/android-ndk

