from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post

# Create your tests here.

class TestView(TestCase):  #고정적 (테스트하는 것 같으니까)
    def setUp(self):
        self.client = Client()
    #위 잘 가져오기

    def test_post_list(self):
        #1.1. 포스트 목록 페이지 가져오기 html 페이지가 가져와지지 않을 경우 오류 남
        response = self.client.get('/blog/')
        #1.2 정상적으로 페이지가 로드된다
        self.assertEqual(response.status_code, 200)
        #정상, 에러코드가 404면 코드는 문제 없으나 원하는 위치에 없음(페이지 없음)
        # 500이면 내부적? 오류
        #1.3 페이지 타이틀은 'BLog'
        soup=BeautifulSoup(response.content, 'html.parser')  #고정으로 작성 모든 텍스트를 가져와 html 객체에 넣는다
        self.assertEqual(soup.title.text, 'Blog')

        print("------load Blog----------") #정상적으로 완료되면 출력됨

        #1.4네비게이션 바가 있다.
        navbar=soup.nav
        #1.5 Blog, About Me 라는 문구가 네비겨이션 바에 있다.
        self.assertIn('Blog', navbar.text)
        self.assertIn('About Me', navbar.text)

        #2.1 포스트가 하나도 없다면
        self.assertEqual(Post.objects.count(), 0)
        #2.2 main area에 '아직 게시물이 없습니다'라는 문구 나타남
        main_area=soup.find('div', id='main-area')
        self.assertIn('아직 게시물이 없습니다', main_area.text)

        #3.1 포스트가 2개 있다면
        post_001=Post.objects.create(
            title='첫 번째 포스트입니다.',
            content='Hello World. We are the world.',
        )
        post_002=Post.objects.create(
            title='두번째 포스트입니다.',
            content='1등이 전부는 아니잖아요',
        )
        self.assertEqual(Post.objects.count(), 2)

        #3.2 포스트 목록 페이지를 새로고침 했을 때
        response=self.client.get('/blog/')
        soup=BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(response.status_code, 200)
        #3.2 main area에 2개의 제목 존재
        main_area=soup.find('div', id=main_area)
        self.assertIn(post_001.title, main_area.text)
        self.assertIn(post_002.title, main_area.text)
        #3.4 '아직 게시물이 없습니다'라는 문구는 더이상 나타나지 않는다.
        self.assertNotIn('아직 게시물이 없습니다', main_area.text)
