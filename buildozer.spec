[app]

# (str) Title of your application
title = Captcha App

# (str) Package name
package.name = captcha_app

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py is located
source.dir = .

# (str) Version of your application
version = 1.0

# (str) Source code where the main.py is located
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,easyocr,opencv,requests

# (str) Presplash of the application
presplash.filename = %(source.include_exts)s

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Supported orientation (one of: landscape, portrait or all)
orientation = portrait

# (int) Minimum API level supported
android.api = 31

# (int) Android NDK version to use
android.ndk = 21b

# (str) Path to a custom keystore to sign your application
#android.keystore = <path-to-keystore>
