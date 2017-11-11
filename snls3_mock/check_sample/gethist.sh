#!/bin/bash

i=1

while [ $i -le 10 ]
    do
        snls=../snls3_mock_CLASSMC_$i.txt
        echo 'getting hist from '$snls
        python PlotErrHist.py $snls figs/hist_$i.png
        i=`expr $i + 1`
    done
