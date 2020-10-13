#cd /gumtree/url_gumtree/url_gumtree/spiders
#mkdir hosni_gumtree
#cd
DATE=`date +%Y-%m-%d-%H-%M-%S`
# 1 Activate Virtual Env
source /home/h.mahmoudi/env3/bin/activate

# 2 GO to the project directory
cd ~/gumtree/url_gumtree/url_gumtree/spiders

# 3 Launch the Crawl
nohup scrapy crawl gumtree_url04_13 -o gumtree_$DATE.csv
