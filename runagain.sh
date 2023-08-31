for x in  `ls ./samples/2harmonics_*.wav `;
do echo $x;
   python -m  encodec $x --force > $x.txt
   emojintrospector read --input $x.txt > $x.emoj
   cat $x.emoj|sort |uniq -c |sort -n > $x.report
 done
