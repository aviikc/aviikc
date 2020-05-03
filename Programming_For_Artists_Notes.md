
# Table of Contents

1.  [Why Use Python](#org161f8f6)
2.  [How Python is Implemented](#orgbf5812c)
3.  [](#org5c94c1c)



<a id="org161f8f6"></a>

# Why Use Python

-   Accessible.Being an open-source language, Python is completely free to download and use. This can already contribute to project cost reductions.Besides that, it requires very little setup to run.
-   Cross platform.Python is supported by all major operating systems: Windows, Linux distributions and Mac OS.
-   Easy to grasp.The reason behind that is a very simple syntax, which in turn reduces syntactical overhead and steepens the learning curve. It is largely recommended as a good choice for a first programming language to learn.
-   Readability.Indeed, Python has a very clear syntax enhanced by a set of punctuation rules and is easy to readand understandbecause it bears close resembles to English language.
-   OOP support.By creating, using and re-using data structures, one can minimizethe amount of coding required to accomplish a certain task.
-   Extensive libraries.Python comes with a massive standard library and extensions for any type of programming tasks.
-   Interpreted. Python is processed at runtime and there is no need to wait for the com-pilation phase to complete thus reducing development time and stimulating the learn-ing process.
-   Large community. Not only Python user community is very large, but also it offers a lot of support, shares resources and in general stimulates the learning process.
-   Transferable. Python is very portable and can work on a wide gamut of various hard-ware devices.
-   Great documentation. Python is equipped with comprehensive documentation mak-ing problem solving much easier.


<a id="orgbf5812c"></a>

# How Python is Implemented

1.Automation. 

It is often alleged that automation of repetitive and routine tasks is one of the main reasons why Python found its way intoVFXindustry. Suchtasksmight involve any number of monotonous animations, e.g. copy-pasting animation       keyframes, set-ting up similar character rigs, copying light setup from one scene to another, setting up and adjusting several scene parameters, defining output destinationand many differ-ent others. As long as the taskcan be described as an algorithm, it can bescripted in Python. The ultimate goalis to automate the workflow as much as possible in order to remove the burden from the artists and let them focus on art creation.Another often overlookedaspect has to do with thehuman error component, as people do occasionally make mistakes, typos, spelling errors and such. By automating some of the tasks, one can reduce the human error component that in turn would result in much more predictable outcome.

2.Software extension.

Some post-production companies have a dedicated R&D depart-ment that works on proprietaryin-house tools andalsoextends the commercial soft-ware  by  addressingthe needs of artistswho  depending  on the  complexity  of  a  task assigned might require an off-the-shelf solution. Granted that the majority of 3D pro-grams have a Python API, which allows to communicate with the core of software, in conjunction with rich Python library modulespresents the environment where there are countless possibilitiesto build new tools, scripts and plugins to go far beyond the de-fault feature-set. Specifically, it is commonly adopted in the character rigging process, when  technical  directors  need  to  build  complex  dependencies  between  partsof  a modeland controlor constraintsystems and Python is used to link them together.

3.Pipeline/workflowenhancers. 

There is a vast array of utilities that can be madewith Python and be helpful invisual effects productions, that are not directly related to DCC software. For example, various scripts that can execute shell commands forvarious purposes: scan directories and delete bitmap fileswith specific metadata, batch con-vert files, resize images that match a certain criterion. There are also multiple modules to work with image processing in Python. Such include OpenImageIO, OpenEXRandPythonMagick. They allow for basic analysis and manipulation of both image data and metadata. Apart from that,there also modules for color manipulationthat enablesto convert image from one color space to another or linearize the image OpenColorIO and ColorPy. Although most established VFX studios rely on comprehensive DAM systems,  individual  artists  and start-upscanmake  use  of  Python  programming and develop their own solutions in the matter of file transferring, management and synchro-nization. The same applies for project management.It is not uncommon for a facility to have some small desktop apps that artists would use to track jobs, deadlines and deliver project statisticsfor benchmarking. By and large, Python can be integrated into any aspect of the post-production–it all comesdownto the specific problem at hand.

4.Smoothstagetransition. 

Bringing up the fact, that in certain cases every stage of pipe-line is done in different software and sometimes a single stage can be completed with a  diverse  assortment  of  tools, the  issue  ofmanagement  and  configuration  of  digital content creation software occurs.Most of the tools used in VFX productionwerenot developed to easilyinteractwith each other, besidesmaybesupporting a few common file  formats. In  this  scenario  Python  serves  the  underlying  role  of theglue  that  ties pieces of  assets together.  There  are  different  Python  modules  for  content  and  data transfer  across distinctive  software  tools.  Alembicgl  isa module  that  allows  to  work with alembic, a file format often used for geometry caching. Similarly, pyopenvdb is a module that provides withan access to VDBvolumesdata management with Pytho


<a id="org5c94c1c"></a>

# 

