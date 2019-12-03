#!/bin/bash
# chech if today is a deadline for new training cycle and send mail to given emails
# cron needs to be set up to run this script once a day
#
# prereq:
#       - mail server on linux machine
#       - cron to run this script once a day
# vars:
#       - today = current date in yyyy-mm-dd format
#       - cykly = array of dates when new training cycle start
#       - recipients = array of emals to send notification to
#       - msg = mesage to send via email


today=$(date +%Y-%m-%d)

cycles=('2019-12-30' '2020-01-27' '2020-02-24' '2020-03-23' '2020-04-20' '2020-05-18' '2020-06-15' '2020-07-13' '2020-08-10' '2020-09-07' '2020-10-05')

recipients=('otakar.hirs@gmail.com')

msg="Ahoj,\nvčera skončil další cyklus. Pokud nechceš smutného či naštveného Šéďu, měl bys vyplnit deníček.\nhttp://reprezentace.orientacnibeh.cz/treninkovy-denik\n\nPeepPoop"

for novy_cyklus in "${cycles[@]}" ; do

    if [ "$today" == "$novy_cyklus" ]; then

        for email in "${recipients[@]}" ; do

                echo -e $msg | mail -s "Vyplň deníček" -S "from=reprebot@zabiny.club" $email

        done

    fi

done

