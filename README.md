## SET UP

- [x] poetry 설정
  - [x] poetry init
  - [x] poetry add django
- [x] start project

- [x] django 설정
  - [x] run server
  - [x] `django_session` 테이블 생성
  - [x] super user 생성

<br>

## 모델 생성

- [x] `bands` 모델 생성
  - [x] 필드 생성
    - [x] 사진, 이름, 결성일, 데뷔일, 장르, 구성원, 대표곡, 앨범, 수상내역 필드
  - [x] admin 추가

<br>

- [x] `comments` 모델 생성
  - [x] 필드 생성
    - [x] 내용, 작성 시간 필드
  - [x] admin 추가

<br>

## REST API

### `bands`

- [ ] **GET /api/v1/bands**
  - [ ] **view**: 모든 밴드 리스트를 반환
  - [ ] **serializer**: `BandSerializer`(밴드 데이터 직렬화)

<br>

- [ ] **GET /api/v1/bands/{id}**
  - [ ] **view**: 특정 밴드 데이터를 반환
  - [ ] **serializer**: `BandDetailSerializer`(특정 밴드 데이터 직렬화)

<br>

<!-- - [ ] **PUT /api/v1/bands/{id}**
  - [ ] **view**: 특정 밴드 데이터를 수정
  - [ ] **serializer**: `BandDetailSerializer` -->

<br>

- [ ] **DELETE /api/v1/bands/{id}**
  - [ ] **view**: 특정 밴드 데이터를 삭제
  - [ ] **serializer**: `BandDetailSerializer`

<br>

### `comments`

- [ ] **GET /api/v1/comments**
  - [ ] **view**: 모든 댓글 데이터를 반환
  - [ ] **serializer**: `CommentSerializer`(댓글 데이터 직렬화)

<br>

- [ ] **POST /api/v1/comments**
  - [ ] **view**: 새 댓글 작성
  - [ ] **serializer**: `CommentSerializer`

<br>

- [ ] **GET /api/v1/comments/{id}**
  - [ ] **view**: 특정 댓글 데이터를 반환
  - [ ] **serializer**: `CommentDetailSerializer`(특정 댓글 데이터 직렬화)

<br>

- [ ] **DELETE /api/v1/comments/{id}**
  - [ ] **view**: 특정 댓글 데이터를 삭제
  - [ ] **serializer**: `CommentDetailSerializer`
