# Secured_Post

비밀번호를 이용한 게시글 서비스
<br>
<br>

## MVP Service
유저가 이모지, 비밀번호를 포함한 게시글을 작성하는 서비스로 아래와 같은 기능을 제공한다.

- 유저 : 구현하지 않음 ( 분석된 요구사항에서 필요로 하지 않음 )
- 게시글
    - **R**ead : All
    - **C**reate : All (이모지, 작성하는 게시글의 비밀번호 포함하여 작성한다.)
        - 이모지 적용 방법 : (제목, 내용에)정규표현식을 적용
    - **U**pdate : C에서 입력한 비밀번호를 통과해야만 가능
    - **D**elete : C에서 입력한 비밀번호를 통과해야만 가능
<br>

## 💻 기술 스택

<div style='flex'>
<img src="https://img.shields.io/badge/Python3.9.5-3776AB?style=for-the-badge&logo=Python&logoColor=white" >
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">
<img src="https://img.shields.io/badge/Django REST framework-092E20?style=for-the-badge&logo=Django REST framework&logoColor=white">
</div>
<br>
<br>

## 👉 ERD

<img width="500" src="https://user-images.githubusercontent.com/101394490/188778444-95b9ce69-697b-4d75-bab7-2880f605a994.png" />
<br>

## 🙏 API 명세서

### [API 링크](https://www.notion.so/617c8233819e4cc58a47979f609ac178) 

### **API 이미지 (예시)**
 <img width="785" src="https://user-images.githubusercontent.com/101394490/188778870-c50b268f-013e-4bdc-b1b2-87aae520afc8.png" />

<details>
<summary>API 상세보기 이미지</summary> <br>
<div markdown="1">
 <img width="500" src="https://user-images.githubusercontent.com/101394490/188778490-1ad715ab-cad5-48cd-ae29-1e15da7d2498.png" />
</div>
</details>
<br>

## 📌 컨벤션

### ❓ Commit Message

- feat/ : 새로운 기능 추가/수정/삭제
- enhan/ : 기존 코드에 기능을 추가하거나 기능을 강화할 때
- refac/ : 코드 리팩토링,버그 수정
- test/ : 테스트 코드/기능 추가
- edit/ : 파일을 수정한 경우(파일위치변경, 파일이름 변경, 삭제)

### ❓ Naming

- Class : Pascal
- Variable : Snake
- Function : Snake
- Constant : Pascal + Snake

### ❓ 주석

- Docstring을 활용하여 클래스와 함수단위에 설명을 적어주도록 하자.
- input/output을 명시하여 문서 없이 코드만으로 어떠한 결과가 나오는지 알 수 있도록 하자.

### 🚷 벼락치기의 규칙

- 컨벤션 지키기
- Commit 단위 지키기
- 말 이쁘게하기
- 문제를 마주하여 트러블을 겪었다면, 어떻게 해결을 했는지 공유를 해주기
- 각자의 작업을 미리 작성을 하여서 각자의 작업을 공유하기
<br>

## 💻 트러블슈팅

### 1. 게시글 작성 기능 TDD로 구현
: post_create_service 함수를 TDD로 구현하는데 있어서 익숙하지 않아서 어려움이 많았다.

> 작성 루틴 : `test` 코드 작성 ->  `test` 통과하기 위한 `service` 코드 작성 -> `error` 코드 확인 -> `error` 핸들링 & `test` 통과 확인 -> 코드 리팩토링 

> ex) 
> 1. `test` 코드 작성  
> <img width="400" src="https://user-images.githubusercontent.com/68724828/188860253-21cdc394-1c57-4d50-bda5-de154f2bdf9b.png" />  

>2. `test` 통과하기 위한 `service` 코드 작성  
> <img width="500" src="https://user-images.githubusercontent.com/68724828/188860654-01bc5b67-149d-4e8a-b52e-edb486a0f1a8.png" />  

> 3. `error` 코드 확인  
> <img width="600" src="https://user-images.githubusercontent.com/68724828/188860984-a3bad1b1-db29-4de6-9968-8e96182a6dfa.png" />  

> 4. `error` 핸들링 & `test` 통과 확인  
> <img width="600" src="https://user-images.githubusercontent.com/68724828/188861254-c64e60f2-4241-4325-8236-63845e8be86d.png" />  
> <img width="600" src="https://user-images.githubusercontent.com/68724828/188862309-1cd82a97-d854-4e28-96ad-0ecaa1306a15.png" />  


### 2. View Error 메시지 핸들링
: `service`에서 중요 메소드를 구현하고 `View`에서 `request data`, `response`에 따른 `error`를 핸들링하는데 있어서 `error` 메시지를 처리하는데 어려움이 있었다.

> `try` `except` 구문에서 `exceptions`을 이용해 `error` 메시지 분석 & 핸들링 
>
> <img width="600" src="https://user-images.githubusercontent.com/68724828/188863066-e14cb83e-3a0d-426a-8406-a96684419bcd.png" />  

