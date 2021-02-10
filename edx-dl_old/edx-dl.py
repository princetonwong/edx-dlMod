#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from edx_dl import edx_dl

'''
You can access 11 courses
 1 - Philosophy and Critical Thinking [course-v1:UQx+META101x+1T2020/co]
     https://courses.edx.org/courses/course-v1:UQx+META101x+1T2020/course/
 2 - Money, Markets, and Morals [course-v1:HarvardX+MMM+2T2020/co]
     https://courses.edx.org/courses/course-v1:HarvardX+MMM+2T2020/course/
 3 - Financial Management in Organizations [course-v1:USMx+AFM603x+3T2020/co]
     https://courses.edx.org/courses/course-v1:USMx+AFM603x+3T2020/course/
 4 - Databases: Relational Databases and SQL [course-v1:StanfordOnline+SOE.YDB-SQL0001+2T2020/co]
     https://courses.edx.org/courses/course-v1:StanfordOnline+SOE.YDB-SQL0001+2T2020/course/
 5 - Databases: Modeling and Theory [course-v1:StanfordOnline+SOE.YDB-MDL_THEORY0001+2T2020/co]
     https://courses.edx.org/courses/course-v1:StanfordOnline+SOE.YDB-MDL_THEORY0001+2T2020/course/
 6 - UML Class Diagrams for Software Engineering [course-v1:KULeuvenX+UMLx+3T2020/co]
     https://courses.edx.org/courses/course-v1:KULeuvenX+UMLx+3T2020/course/
 7 - Introduction to Web Cartography: Part 2 [course-v1:ETHx+WC-02x+3T2018/co]
     https://courses.edx.org/courses/course-v1:ETHx+WC-02x+3T2018/course/
 8 - Foundations of Modern Finance  I [course-v1:MITx+15.415.1x+1T2020/co]
     https://courses.edx.org/courses/course-v1:MITx+15.415.1x+1T2020/course/
 9 - Financial Market Analysis [course-v1:IMFx+FMAx+3T2020/co]
     https://courses.edx.org/courses/course-v1:IMFx+FMAx+3T2020/course/
10 - The Analytics Edge [course-v1:MITx+15.071x+2T2020/co]
     https://courses.edx.org/courses/course-v1:MITx+15.071x+2T2020/course/
11 - Introduction to Web Cartography: Part 1 [course-v1:ETHx+WC-01x+3T2018/co]
     https://courses.edx.org/courses/course-v1:ETHx+WC-01x+3T2018/course/

1 - Introduction to Psychological Research Methods [course-v1:UQx+PSYC1030.4x+1T2021/co]
     https://courses.edx.org/courses/course-v1:UQx+PSYC1030.4x+1T2021/course/
 2 - Introduction to Clinical Psychology [course-v1:UQx+PSYC1030.3x+1T2021/co]
     https://courses.edx.org/courses/course-v1:UQx+PSYC1030.3x+1T2021/course/
 3 - Introduction to Developmental Psychology [course-v1:UQx+PSYC1030.2x+1T2021/co]
     https://courses.edx.org/courses/course-v1:UQx+PSYC1030.2x+1T2021/course/
 4 - Introduction to Social Psychology [course-v1:UQx+PSYC1030.1x+1T2021/co]
     https://courses.edx.org/courses/course-v1:UQx+PSYC1030.1x+1T2021/course/
 5 - Databases: Semistructured Data [course-v1:StanfordOnline+SOE.YDB-SSD0001+2T2020/co]
     https://courses.edx.org/courses/course-v1:StanfordOnline+SOE.YDB-SSD0001+2T2020/course/
 6 - Databases: OLAP and Recursion [course-v1:StanfordOnline+SOE.YDB-OLAP_RECURSION0001+2T2020/co]
     https://courses.edx.org/courses/course-v1:StanfordOnline+SOE.YDB-OLAP_RECURSION0001+2T2020/course/
 7 - Databases: Advanced Topics in SQL [course-v1:StanfordOnline+SOE.YDB-ADVSQL0001+2T2020/co]
     https://courses.edx.org/courses/course-v1:StanfordOnline+SOE.YDB-ADVSQL0001+2T2020/course/
 8 - CS50's Introduction to Artificial Intelligence with Python [course-v1:HarvardX+CS50AI+1T2020/co]
     https://courses.edx.org/courses/course-v1:HarvardX+CS50AI+1T2020/course/
 9 - CS50's Web Programming with Python and JavaScript [course-v1:HarvardX+CS50W+Web/co]
     https://courses.edx.org/courses/course-v1:HarvardX+CS50W+Web/course/
10 - Advanced Power Searching With Google [course-v1:Google+PSWGA1+1T2021/co]
     https://courses.edx.org/courses/course-v1:Google+PSWGA1+1T2021/course/
11 - The Foundations of Happiness at Work [course-v1:BerkeleyX+GG201x+1T2020/co]
     https://courses.edx.org/courses/course-v1:BerkeleyX+GG201x+1T2020/course/
12 - Ideas of the 20th Century [UTAustinX/UT.2.02x/3T2014/co]
     https://courses.edx.org/courses/UTAustinX/UT.2.02x/3T2014/course/
13 - The Great War and Modern Philosophy [course-v1:KULeuvenX+GRAPHx+1T2017/co]
     https://courses.edx.org/courses/course-v1:KULeuvenX+GRAPHx+1T2017/course/
14 - CS50's Introduction to Computer Science [course-v1:HarvardX+CS50+X/co]
     https://courses.edx.org/courses/course-v1:HarvardX+CS50+X/course/
15 - Philosophy and Critical Thinking [course-v1:UQx+META101x+1T2020/co]
     https://courses.edx.org/courses/course-v1:UQx+META101x+1T2020/course/
16 - Databases: Relational Databases and SQL [course-v1:StanfordOnline+SOE.YDB-SQL0001+2T2020/co]
     https://courses.edx.org/courses/course-v1:StanfordOnline+SOE.YDB-SQL0001+2T2020/course/
17 - Databases: Modeling and Theory [course-v1:StanfordOnline+SOE.YDB-MDL_THEORY0001+2T2020/co]
     https://courses.edx.org/courses/course-v1:StanfordOnline+SOE.YDB-MDL_THEORY0001+2T2020/course/
18 - Introduction to Web Cartography: Part 2 [course-v1:ETHx+WC-02x+3T2018/co]
     https://courses.edx.org/courses/course-v1:ETHx+WC-02x+3T2018/course/
19 - Foundations of Modern Finance II [course-v1:MITx+15.415.2x+2T2020/co]
     https://courses.edx.org/courses/course-v1:MITx+15.415.2x+2T2020/course/
20 - Financial Market Analysis [course-v1:IMFx+FMAx+3T2020/co]
     https://courses.edx.org/courses/course-v1:IMFx+FMAx+3T2020/course/
21 - Introduction to Web Cartography: Part 1 [course-v1:ETHx+WC-01x+3T2018/co]
     https://courses.edx.org/courses/course-v1:ETHx+WC-01x+3T2018/course/

'''

if __name__ == '__main__':
    edx_dl.main()
