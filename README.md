# AMMD
此项目是在西门子中国研究院实习期间所做的项目，基于Materials Data Curation System，使用Python以及Django搭建了一个材料数据可视化的平台。

项目结构

目录结构就是典型的django目录结构。

项目：mgi。

应用：admin_mdcs、api、compose、curate、explore、exporter、modules、oai_pmh、user_dashboard、data_mining、data_visual。这些应用对应不同的功能。

其它：bin（）、conf（mongodb配置文件）、scripts（一些功能脚本）、static、templates、utils

开启服务：

$source activate ammd16env

$mongod --config mongodb.conf

$python manage.py runserver

链接：https://github.com/usnistgov/MDCS
