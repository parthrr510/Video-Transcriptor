<h1 align="center">
  <br>
  Video Transcriptor
  <br>
</h1>

<h3 align="center">Live Link: <a href="https://videotranscriptor.herokuapp.com">Link</a></h3>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

<div align="center">

![Python](https://img.shields.io/badge/python-3.9.1-blue)
![Version](https://img.shields.io/badge/version-1.0.0-green)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![License](https://img.shields.io/badge/license-%20GPL--3.0%20-blue)](https://github.com/parthrr510/Video-Transcriptor/blob/main/LICENSE)

</div>

<div align="justify">

> Video Transcriptor is a project which takes a youtube video url as input and basically converts the video into a summarized transcript by using API's and speech recognition libraries and using nlp for the summarization.
</div>


<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#io-screenshots">I/O Screenshots</a> •
  <a href="#flowchart">Methodology Flowchart </a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#license">License</a>
</p>

<div id = "key-features" align="justify">
  
## Key Features

* Summarized Transcript 
  * The user can input a video url of youtube and then get summarized transcript accordingly.
    * The user inputs a video url
    * It gets converted into transcript using Youtube Transcript API or it downloads the audio of the youtube video and then converts the audio into text using Speech Recognition Library.
    * The converted Transcript then uses spacy and nlp and uses word and sentence frequency to display summarized transcript. The length of the trnascript is reduced to 30 percent. 
</div>

<div align="justify" id="io-screenshots">

## Input-Output Screenshots

![I/O Screenshots](https://github.com/parthrr510/Video-Transcriptor/blob/main/images/InputOutput.gif)

</div>

<div align="justify" id = "flowchart">

## Methodology Flowchart

![MainFlowChart](https://github.com/parthrr510/Video-Transcriptor/blob/main/images/FlowChart.png)
</div>
<div id = "how-to-use" align="justify">
  
## How to Use
The steps involved to run the application are:<br>
*You must have git and python installed on your machine*
1. Clone the repository.
2. Create a Virtual Environment using following commands
  ```bash
pip install virtualenv
virtualenv venv
```
3. Install the dependencies from `requirements.txt`
```bash
pip install -r requirements.txt
```
4. Run the server using the following command:
```bash
python manage.py runserver
```
**To make any changes in the project,Create a issue and then a pull request for that issue**

</div>


<div id = "license"  align="justify">
 
## License
 
`Video Transcriptor` is free and open-source software licensed under the GPL-3.0 License.

</div>
