from datetime import datetime
import os
from zipfile import ZipFile


def takeoutParse(arch: str):

    # arch = 'tO.zip'
    destFile = 'latLon.json'

    # with open(arch, 'wb') as t:
        # t.write(binData)

    with ZipFile(arch, 'r') as ar:
        ar.extractall()

    script_dir = os.getcwd()
    rel_path = 'Takeout/Location History/Location History.json'
    abs_file_path = os.path.join(script_dir, rel_path)

    with open(destFile, 'w') as dF:
        with open(abs_file_path, "r") as lH:
            jumpToNext = False
            for line in lH:

                element = line.strip()

                # check for timestamp
                if len(element) > 1 and element[1] == 't':

                    # convert timestamp to date
                    dT = datetime.utcfromtimestamp(int(element[17:30])
                                                   / 1000)

                    # REQUIRES TESTING (filter for past 14 days)
                    # only want dates within past 14 days
                    dTnow = datetime.now()
                    diff = dTnow - dT
                    diffDays = divmod(diff.total_seconds(), 86400)[0]
                    if diffDays > 14:
                        # set boolean to skip until next entry
                        jumpToNext = True
                        continue

                    # reset boolean if we find valid diff
                    else:
                        jumpToNext = False

                    dT = dT.strftime('%Y-%m-%d %H:%M:%S')
                    line = '    "date"' + ' : ' + dT + ',' + '\n'

                if len(element) > 1 and element[1] == 'a':
                    continue

                if len(element) > 1 and element[1] == 'v':
                    continue

                if len(element) > 1 and element[1] == 'h':
                    continue

                if jumpToNext:
                    continue

                dF.write(line)

    return destFile
