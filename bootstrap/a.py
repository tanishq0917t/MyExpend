import subprocess
a=[
"bootstrap.css",
"bootstrap.css.map",
"bootstrap-grid.css",
"bootstrap-grid.css.map",
"bootstrap-grid.min.css",
"bootstrap-grid.min.css.map",
"bootstrap-grid.rtl.css",
"bootstrap-grid.rtl.css.map",
"bootstrap-grid.rtl.min.css",
"bootstrap-grid.rtl.min.css.map",
"bootstrap.min.css",
"bootstrap.min.css.map",
"bootstrap-reboot.css",
"bootstrap-reboot.css.map",
"bootstrap-reboot.min.css",
"bootstrap-reboot.min.css.map",
"bootstrap-reboot.rtl.css",
"bootstrap-reboot.rtl.css.map",
"bootstrap-reboot.rtl.min.css",
"bootstrap-reboot.rtl.min.css.map",
"bootstrap.rtl.css",
"bootstrap.rtl.css.map",
"bootstrap.rtl.min.css",
"bootstrap.rtl.min.css.map",
"bootstrap-utilities.css",
"bootstrap-utilities.css.map",
"bootstrap-utilities.min.css",
"bootstrap-utilities.min.css.map",
"bootstrap-utilities.rtl.css",
"bootstrap-utilities.rtl.css.map",
"bootstrap-utilities.rtl.min.css",
"bootstrap-utilities.rtl.min.css.map"
]

for i in a:
    subprocess.run(["wget",f"https://github.com/tanishq1710h/MyExpend/tree/main/bootstrap/css/{i}"])
