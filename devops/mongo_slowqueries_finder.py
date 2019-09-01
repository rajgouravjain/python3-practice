def log_finder(file_path, latency):
    with open(file_path, 'r') as m:
        try:
            g1 = (content for content in m if int(content.split()[-1].split('ms')[0]) > int(latency))
        except:
            pass

        for i in g1:
            print ix


if __name__ == '__main__':
    ## sanitize your logs using below command before parsing to to python
    #grep  "2018-06-01T07\|2018-06-01T08" /var/log/mongodb/mongod.log  |grep "I COMMAND" | grep   'ms$' > c.log
    log_finder('c.log', 1000)
    