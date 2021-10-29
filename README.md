Account API는 회원정보 관리 API 입니다. 
회원등록, 로그인, 회원정보 보기, 로그아웃, 패스워드 수정의 기능이 있습니다. 

Python + Django를 기반으로 MTV패턴에 따라 클래스들을 구성했습니다.
이는 MSA(Micro Service Architecture)의 한 API로서,

KT클라우드에서 Account-API의 Docker 이미지를 컨테이너로 실행하고, 
Kong(API Gateway)에 Microservice로서 등록할 예정입니다.
