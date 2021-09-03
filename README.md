# seqdbmaker
Scripts to create a sequence database



```
$ python3 download.py tailspike
```

The \*.tar.gz file will have lots of things that UniProt 'thinks' are tailspike:
```
$ zcat tailspike.fasta.gz | grep "^>" | head
>sp|Q8CWC7|PIC_ECOL6 Serine protease pic autotransporter OS=Escherichia coli O6:H1 (strain CFT073 / ATCC 700928 / UPEC) OX=199310 GN=pic PE=3 SV=1
>sp|P24328|PERT_BORPA Pertactin autotransporter OS=Bordetella parapertussis (strain 12822 / ATCC BAA-587 / NCTC 13253) OX=257311 GN=prn PE=3 SV=1
>sp|P14283|PERT_BORPE Pertactin autotransporter OS=Bordetella pertussis (strain Tohama I / ATCC BAA-589 / NCTC 13251) OX=257313 GN=prn PE=1 SV=3
>sp|Q8FDW4|SAT_ECOL6 Serine protease sat autotransporter OS=Escherichia coli O6:H1 (strain CFT073 / ATCC 700928 / UPEC) OX=199310 GN=sat PE=1 SV=2
>sp|P09790|IGA_NEIGO IgA-specific serine endopeptidase autotransporter OS=Neisseria gonorrhoeae OX=485 GN=iga PE=1 SV=1
>sp|P44969|IGA0_HAEIN Immunoglobulin A1 protease autotransporter OS=Haemophilus influenzae (strain ATCC 51907 / DSM 11121 / KW20 / Rd) OX=71421 GN=iga PE=1 SV=1
>sp|P35837|NEEDL_BPP22 Tail needle protein gp26 OS=Salmonella phage P22 OX=10754 GN=26 PE=1 SV=2
>sp|Q9Y2G1|MYRF_HUMAN Myelin regulatory factor OS=Homo sapiens OX=9606 GN=MYRF PE=1 SV=3
>sp|Q8X621|YDHQ_ECO57 Uncharacterized protein YdhQ OS=Escherichia coli O157:H7 OX=83334 GN=ydhQ PE=4 SV=1
>sp|D2TV88|Y1121_CITRI Probable autotransporter ROD_p1121 OS=Citrobacter rodentium (strain ICC168) OX=637910 GN=ROD_p1121 PE=1 SV=1
```

So you have to clean the file using the script with INCLUDE words:
```
$ python3 clean.py tailspike.fasta.gz --include "tailspike|tail spike" | grep "^>" | head
>tr|A0A7L8YR65|A0A7L8YR65_9VIRU Tailspike protein OS=Escherichia phage HF4s OX=2775262 GN=HF4s_0015 PE=4 SV=1
>tr|A0A7G5CK66|A0A7G5CK66_9VIRU Tailspike OS=Mu-like cryoconite phage AB09 OX=2761371 PE=4 SV=1
>tr|A0A7T8EPR6|A0A7T8EPR6_9VIRU Neck appendage protein/tailspike protein OS=Bacillus phage BSTP5 OX=2801530 GN=BSTP5_011 PE=4 SV=1
>tr|D2A7Z7|D2A7Z7_SHIF2 Tail spike protein OS=Shigella flexneri serotype X (strain 2002017) OX=591020 GN=SFxv_0352 PE=4 SV=1
>tr|A0A7U3Z2M7|A0A7U3Z2M7_9GAMM P22 tailspike protein head-binding protein OS=Serratia sp. AS13 OX=768493 GN=SerAS13_2679 PE=4 SV=1
>tr|A0A6C7I721|A0A6C7I721_SALTD Tail spike protein OS=Salmonella typhimurium (strain D23580) OX=568708 GN=STMMW_03901 PE=4 SV=1
>tr|C4K6V6|C4K6V6_HAMD5 APSE-2 prophage tail spike protein gp9 OS=Hamiltonella defensa subsp. Acyrthosiphon pisum (strain 5AT) OX=572265 GN=P36 PE=4 SV=1
>tr|A0A6C7I4K4|A0A6C7I4K4_SALPK Tailspike OS=Salmonella paratyphi A (strain AKU_12601) OX=554290 GN=SSPA2227 PE=4 SV=1
>tr|A0A1W5DLM4|A0A1W5DLM4_9GAMM p22 tailspike protein head-binding protein OS=Serratia proteamaculans OX=28151 GN=SPRA44_360028 PE=4 SV=1
>tr|A0A7H4L6T3|A0A7H4L6T3_9DELT Phage P22 tailspike protein like OS=Desulfovibrio sp. G11 OX=631220 GN=DSVG11_1924 PE=4 SV=1
```


You can also EXCLUDE words:
```
$ python3 clean.py tailspike.fasta.gz --include "tailspike|tail spike" --exclude "head-binding" | grep "^>" | head
>tr|A0A7L8YR65|A0A7L8YR65_9VIRU Tailspike protein OS=Escherichia phage HF4s OX=2775262 GN=HF4s_0015 PE=4 SV=1
>tr|A0A7G5CK66|A0A7G5CK66_9VIRU Tailspike OS=Mu-like cryoconite phage AB09 OX=2761371 PE=4 SV=1
>tr|A0A7T8EPR6|A0A7T8EPR6_9VIRU Neck appendage protein/tailspike protein OS=Bacillus phage BSTP5 OX=2801530 GN=BSTP5_011 PE=4 SV=1
>tr|D2A7Z7|D2A7Z7_SHIF2 Tail spike protein OS=Shigella flexneri serotype X (strain 2002017) OX=591020 GN=SFxv_0352 PE=4 SV=1
>tr|A0A6C7I721|A0A6C7I721_SALTD Tail spike protein OS=Salmonella typhimurium (strain D23580) OX=568708 GN=STMMW_03901 PE=4 SV=1
>tr|C4K6V6|C4K6V6_HAMD5 APSE-2 prophage tail spike protein gp9 OS=Hamiltonella defensa subsp. Acyrthosiphon pisum (strain 5AT) OX=572265 GN=P36 PE=4 SV=1
>tr|A0A6C7I4K4|A0A6C7I4K4_SALPK Tailspike OS=Salmonella paratyphi A (strain AKU_12601) OX=554290 GN=SSPA2227 PE=4 SV=1
>tr|A0A7H4L6T3|A0A7H4L6T3_9DELT Phage P22 tailspike protein like OS=Desulfovibrio sp. G11 OX=631220 GN=DSVG11_1924 PE=4 SV=1
>tr|A0A7H4L8Y2|A0A7H4L8Y2_9DELT Phage P22 tailspike protein OS=Desulfovibrio sp. G11 OX=631220 GN=DSVG11_2735 PE=4 SV=1
>tr|A0A328TQW2|A0A328TQW2_9GAMM Tail spike protein OS=Candidatus Erwinia dacicola OX=252393 GN=ACZ87_00149 PE=4 SV=1
```

