# 11th_DRF_Session

## 1. 클론하기

클론할 폴더 생성 후 vs code 실행

```
git clone https://github.com/likelionsg/11th_DRF_Session.git .
```

## 2. 가상환경 생성

윈도우는 git bash 터미널에서 해주세요

```
mkdir .venv
pipenv install
pipenv shell
```

## 3. 마이그레이트

```
python3 manage.py makemigrations
python3 manage.py migrate --run-syncdb
```

## 4. 어드민 계정 생성

```
python3 manage.py createsuperuser
```

## 5. 원격 브랜치 가져오기
```
git checkout -b blogapiview origin/blogapiview
git checkout -b viewset origin/viewset
git checkout -b router origin/router
git checkout -b override origin/override
git switch main
```
