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

[buildozer]
log_level = 2
warn_on_root = 1

[app.android]
android.sdk_path = /home/runner/work/EmployeeTrackerApp/EmployeeTrackerApp/android-sdk
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b
