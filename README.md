# 참! 참! 참! 게임

<br>
<p align='center'>
<img src="https://capsule-render.vercel.app/api?type=soft&color=auto&height=200&section=header&text=ELCO%20Exhibition&fontSize=90" />
<img src='https://raw.githubusercontent.com/innovationacademy-kr/our42vent/31b47343ee2021cfc653ba9d7adaf4919b072416/public/assets/images/our42vent_logo_black.svg#gh-light-mode-only' alt='our42vent_logo_white' width='200' height='' style='background:#13171d'/>
</p>
<p align='center'>
  <b><em>
    2022 ELCO 전시회 - 참참참 게임<br>
    NOV/08/2022 - NOV/10/2022<br>
    [국민대학교](https://www.kookmin.ac.kr/user/index.do)
    </em>
  </b>
</p>



<p align='center'>
<a href="https://www.raspberrypi.org/"><img src="https://img.shields.io/badge/-RaspberryPi-C51A4A?style=for-the-badge&logo=Raspberry-Pi"/></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/static/v1?style=for-the-badge&message=Python&color=3776AB&logo=Python&logoColor=FFFFFF&label="/></a>
</p>


## :stuck_out_tongue_closed_eyes: 팀장
|역할|학번|팀명|
|------|:---:|---|
|재학생|19|이창근|
|재학생|19|이지성|
|재학생|19|최제광|                       

## :stuck_out_tongue_closed_eyes: 팀원
|역할|학번|팀명|
|------|:---:|---|                    
|신입생|22|김은수|
|신입생|22|김한결|  
|신입생|22|반석현|
|신입생|22|박지영|  
|신입생|22|유민아|
|신입생|22|이종민|
|신입생|22|이진열| 

## ✨ 개발 동기

  > 관객 참여형 전시회 부스를 만들어보고자 2021년 전세계에서 유행했던 넷플릭스 오징어게임을 오마주해서 전시회에 방문한 관객들이 게임을 적극적으로 참여할 수 있도록 '참참참 게임' 기계를 구상하게 되었습니다. 2학년 팀장 3명이서 2학년 교과과정에서는 배우지 못했던 경험들을 하고자 Python과 OpenCV를 공부하고 3d 프린팅을 공부하여 하드웨어를 제작해보았습니다.  관객의 얼굴을 영상처리를 이용하여 방향을 인식하고 서보모터를 제어하여 참참참 게임을 진행하는 구상을 해봤습니다.

## :bulb: Introduction

- **🌟 OpenCV**

  > ‘참참참 게임’을 만들기 위해 OpenCV를 이용하여 영상처리를 하였습니다. 게임을 실행시키면 웹캠이 앞에 게임 플레이어를 인식한 영상을 실시간으로 받아오기 시작합니다. 받아온 영상에서 Python, OpenCV를 통해 사람의 얼굴을 인식하며, 얼굴의 각도 및 방향을 인식합니다. 영상을 통해 인식한 사람의 얼굴 방향과 컴퓨터의 난수를 통해 랜덤으로 출력한 얼굴방향을 통해 컴퓨터와 사람간의 게임을 진행합니다.

- **🌟 Pygame**

  > Pygame라이브러리를 이용하여 게임을 만들었으며, 얼굴을 인식하는데 있어 Mediapipe를 이용하였습니다. 3d프린터를 이용하여 컴퓨터의 팔, 진행자의 얼굴, 게임 조이스틱과 같은 하드웨어를 제작했습니다. 추가로 GPIO를 이용하여 서보모터로 컴퓨터의  제어하였습니다.

- **🌟 Rule**

  > 게임이 진행되면 진행자의 참참참 소리에 얼굴 방향을 왼쪽, 오른쪽 및 가운데로 틀어 손을 피해야 합니다. 랜덤으로 틀어진 손의 방향과 게임 플레이어의 얼굴 방향이 다르면 1점씩 점수를 얻게 되고, 손의 방향과 게임 플레이어의 얼굴 방향이 같으면 게임 오버가 됩니다.
