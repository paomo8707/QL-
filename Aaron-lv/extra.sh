#!/usr/bin/env bash

## 添加你需要重启自动执行的任意命令，比如 ql repo
## 安装node依赖使用 pnpm install -g xxx xxx
## 安装python依赖使用 pip3 install xxx

ql repo https://github.com/smiek2121/scripts.git "jd_|gua_" "gua_cleancart.js|gua_wealth_island_help.js|jd_sign_graphics.js|gua_ddworld.js|jd_joy_steal.js|jd_sendBeans.js|gua_wealth_island.js|jd_joy.js" "ZooFaker_Necklace.js|JDJRValidator_Pure.js|sign_graphics_validate.js|cleancart_activity.js|jdCookie.js|sendNotify.js"
ql repo https://github.com/KingRan/KR.git "jd_|jx_|jdCookie" "activity|backUp" "^jd[^_]|USER|utils|function|sign|sendNotify|ql|JDJR"
ql repo https://github.com/feverrun/my_scripts.git "jd_|jx_|jddj_|getCookie|getJDCookie" "backUp" "^(jd|JD|JS)[^_]|USER|sendNotify|utils"
task disableDuplicateTasksImplement.py

