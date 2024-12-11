## SET UP

- [x] poetry 설정
  - [x] poetry init
  - [x] poetry add django
- [x] start project

- [x] django 설정
  - [x] run server
  - [x] `django_session` 테이블 생성
  - [x] super user 생성
  - [x] django-cors-headers 설치

<br>

## 모델 생성

- [x] `band` 모델 생성
  - [x] 필드 생성
    - [x] 사진, 이름, 결성일, 데뷔일, 장르, 구성원, 대표곡, 앨범, 수상내역 필드
  - [x] admin 추가

<br>

- [x] `comment` 모델 생성
  - [x] 필드 생성
    - [x] 내용, 작성 시간 필드
  - [x] admin 추가

<br>

- [ ] `user` 모델 생성
  - [ ] 필드 생성
    - [ ] 사진, 아이디, 비밀번호, 즐겨찾기
  - [ ] 즐겨찾기 view 추가
    - [ ] 필드 생성
      - [ ] 즐겨찾기 밴드 id, 이름, 사진 필드
  - [ ] admin 추가

<br>

## REST API

### `band`

- [x] **GET /api/v1/bands**
  - [x] **view**: 모든 밴드 리스트를 반환
  - [x] **serializer**: `BandDetailSerializer`(밴드 데이터 직렬화)

<br>

- [x] **GET /api/v1/bands/{id}**
  - [x] **view**: 특정 밴드 데이터를 반환
  - [x] **serializer**: `BandDetailSerializer`

<br>

<!-- - [ ] **PUT /api/v1/bands/{id}**
  - [ ] **view**: 특정 밴드 데이터를 수정
  - [ ] **serializer**: `BandDetailSerializer` -->

<br>

- [x] **DELETE /api/v1/bands/{id}**
  - [x] **view**: 특정 밴드 데이터를 삭제
  - [x] **serializer**: `BandDetailSerializer`

<br>

### `comment`

- [x] **GET /api/v1/comments**
  - [x] **view**: 모든 댓글 데이터를 반환
  - [x] **serializer**: `CommentSerializer`(댓글 데이터 직렬화)

<br>

- [x] **POST /api/v1/comments**
  - [x] **view**: 새 댓글 작성
  - [x] **serializer**: `CommentSerializer`

<br>

- [x] **GET /api/v1/comments/{id}**
  - [x] **view**: 특정 댓글 데이터를 반환
  - [x] **serializer**: `CommentDetailSerializer`(특정 댓글 데이터 직렬화)

<br>

- [x] **DELETE /api/v1/comments/{id}**
  - [x] **view**: 특정 댓글 데이터를 삭제
  - [x] **serializer**: `CommentDetailSerializer`

<br>

### `user`

- [ ] **GET /api/v1/users**
  - [ ] **view**: 모든 유저 데이터 반환
  - [ ] **serializer**: `UserSerializer`(모든 유저 데이터 직렬화)

<br>

- [ ] **POST /api/v1/users**
  - [ ] **view**: 새로운 유저 추가
  - [ ] **serializer**: `UserSerializer`

<br>

- [ ] **GET /api/v1/users/{id}**
  - [ ] **view**: 특정 유저 데이터를 반환
  - [ ] **serializer**: `UserDetailSerializer`(특정 유저 데이터 직렬화)

<br>

- [ ] **PUT /api/v1/users/{id}**
  - [ ] **view**: 특정 유저 데이터 변경
  - [ ] **serializer**: `UserDetailSerializer`

<br>

- [ ] **DELETE /api/v1/users/{id}**
  - [ ] **view**: 특정 유저 데이터 삭제
  - [ ] **serializer**: `UserDetailSerializer`

<br>

- [ ] **GET /api/v1/users/{id}/likes**
  - [ ] **view**: 특정 유저 즐겨찾기 데이터를 반환
  - [ ] **serializer**: `UserDetailLikeserializer`(특정 유저 즐겨찾기 데이터 직렬화)
