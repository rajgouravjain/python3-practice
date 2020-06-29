import re
import matplotlib.pyplot as plt
import pandas as pd
import sys

def generate_log_sequence(filename):
    with open(filename,'r') as fp:
        multiline = False
        msg = ""
        for line in fp:
            if re.search('Everything looks good$',line):

                #line = "2019/09/12 09:00:00 [PID 1234] [234ms] [UID xS2671] [INFO] /home Everything looks good"
                date, ttime, pid_tmp, pid, response_time, uid_tmp, uid, log_level, url , *msg  = tuple(line.split())
                pid = pid.rstrip("]")
                uid = uid.rstrip("]")
                response_time = response_time.strip("][ms")
                log_level = log_level.strip("][")
                msg = " ".join(msg)
                #print(msg)
                multiline = False
                #date_time = time.strptime(date + " " + ttime, '%Y-%m-%d %H:%M:%S.%f' )
                date_time = date + " " + ttime
                yield (date_time,pid,response_time,uid,log_level,url,msg)
                #print(date,time,pid,response_time,uid,log_level,url,msg)

            else :
                if re.search('^\d\d\d\d',line):
                    if multiline == True :
                        yield (date_time, pid, response_time, uid, log_level, url, msg)
                    ##Then its a new line, Save variables
                    date, ttime, pid_tmp, pid, response_time, uid_tmp, uid, log_level, url, *msg = tuple(line.split())
                    pid = pid.rstrip("]")
                    uid = uid.rstrip("]")
                    response_time = response_time.strip("ms][")
                    log_level = log_level.strip("][")
                    date_time = date + " " + ttime
                    # date_time = time.strptime(date + " " + ttime, '%Y-%m-%d %H:%M:%S.%f' )
                    msg = " ".join(msg)
                    multiline = False
                else:
                    ##Else its a multiline, tag it and append it to msg.
                    multiline = True
                    msg = msg + ' ' + line.strip()



def generate_error_sequence(log_sequences):
    for log_sequence in log_sequences:
        if log_sequence[4] == 'ERROR':
            yield log_sequence

def plot_histogram():
    pass


if __name__ == '__main__' :

    log_sequences = generate_log_sequence('AIout.log')
    log_sequence_list = [x for x in log_sequences]
    df = pd.DataFrame(log_sequence_list, columns=['date_time','pid','response_time','uid','log_level','url','msg'])

    df['date_time'] = pd.to_datetime(df['date_time'],infer_datetime_format=True)
    df[['pid', 'response_time']] = df[['pid', 'response_time']].apply(pd.to_numeric)
    df['msg'].astype(str)

    #print(df.dtypes)
    #print(df.describe())

    df_success = df[df['msg'].str.match("Everything looks good$")]
    #print(df_success.describe())

    df_error = df[df['msg'].str.match("Everything looks good$") == False]
    #print(df_error.describe())
    print(df_success['response_time'].quantile(q=0.5))
    print(df_success['response_time'].quantile(q=0.9))
    print(df_success['response_time'].quantile(q=0.95))

    plt.figure()
    plt.hist(df_error['date_time'],bins=150)
    plt.show()

    print(sys.version_info)
